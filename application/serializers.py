from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from application.models import Chapter, Material
from application.validators import UrlValidator


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"
        validators = [UrlValidator(field="url")]


class ChapterSerializer(serializers.ModelSerializer):
    lesson = MaterialSerializer(source="material_set", many=True, read_only=True)
    material_in_chapter_count = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    def get_lessons_in_course_count(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Chapter
        fields = "__all__"
