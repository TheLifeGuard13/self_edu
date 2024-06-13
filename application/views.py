
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from application.models import Chapter, Material, Question, Answer, Subscription
from application.paginators import ApplicationPaginator
from application.serializers import MaterialSerializer, ChapterSerializer, QuestionSerializer, AnswerSerializer

from users.permissions import IsOwner, IsStaff


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    pagination_class = ApplicationPaginator

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    # def get_permissions(self):
    #     if self.action in ["list", "create", "update", "retrieve", "destroy"]:
    #         self.permission_classes = (IsOwner | IsStaff,)
    #     return super().get_permissions()


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    pagination_class = ApplicationPaginator

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     if user.is_staff:
    #         return queryset
    #     return queryset.filter(owner=user)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    # def get_permissions(self):
    #     if self.action in ["list", "create", "update", "retrieve", "destroy"]:
    #         self.permission_classes = (IsOwner | IsStaff,)
    #     return super().get_permissions()


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = ChapterSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        chapter_id = self.request.data.get("chapter")
        chapter_item = get_object_or_404(Chapter, pk=chapter_id)

        subs_item = Subscription.objects.filter(subscriber=user, chapter=chapter_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(subscriber=user, chapter=chapter_item)
            message = "подписка добавлена"
        # Возвращаем ответ в API
        return Response({"message": message})


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # def get_queryset(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
    #     queryset = super().get_queryset(*args, **kwargs)
    #     return queryset.order_by("?")[:3]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     if user.is_staff:
    #         return queryset
    #     return queryset.filter(owner=user)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    # def get_permissions(self):
    #     if self.action in ["list", "create", "update", "retrieve", "destroy"]:
    #         self.permission_classes = (IsOwner | IsStaff,)
    #     return super().get_permissions()


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    # def get_queryset(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
    #     queryset = super().get_queryset(*args, **kwargs)
    #     return queryset.order_by("?")[:3]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     if user.is_staff:
    #         return queryset
    #     return queryset.filter(owner=user)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    # def get_permissions(self):
    #     if self.action in ["list", "create", "update", "retrieve", "destroy"]:
    #         self.permission_classes = (IsOwner | IsStaff,)
    #     return super().get_permissions()
