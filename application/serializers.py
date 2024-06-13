from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from application.models import Chapter, Material, Question, Answer, Subscription
from application.validators import UrlValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"
        validators = [UrlValidator(field="url")]


class ChapterSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(source="material_set", many=True, read_only=True)
    material_in_chapter_count = SerializerMethodField()
    is_subscribed = SerializerMethodField()
    subscribers = SubscriptionSerializer(source='chapter_for_subscription', many=True, read_only=True)

    def get_material_in_chapter_count(self, obj):
        return obj.material_set.all().count()

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        user = None
        if request:
            user = request.user
        return obj.chapter_for_subscription.filter(subscriber=user).exists()

    class Meta:
        model = Chapter
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
