from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from application.models import Chapter, Material, Subscription
from application.paginators import ApplicationPaginator
from application.serializers import MaterialSerializer, ChapterSerializer, SubscriptionSerializer

from users.permissions import IsStaff


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    pagination_class = ApplicationPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["created", 'id']

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = (IsStaff,)
        else:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    pagination_class = ApplicationPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["created", "id"]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = (IsStaff,)
        else:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        chapter_id = self.request.data.get("chapter")
        chapter_item = get_object_or_404(Chapter, pk=chapter_id)

        subs_item = Subscription.objects.filter(subscriber=user, chapter=chapter_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = "Вы отписались от Раздела с материалами"
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(subscriber=user, chapter=chapter_item)
            message = "Вы подписались на этот Раздел с материалами"
        # Возвращаем ответ в API
        return Response({"message": message})
