from rest_framework import generics, viewsets

from application.models import Chapter, Material
from application.serializers import MaterialSerializer, ChapterSerializer

from users.permissions import IsOwner, IsStaff


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    # serializer_class = HabitSerializer
    pagination_class = ChapterSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_staff:
            return queryset
        return queryset.filter(owner=user)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action in ["list", "create", "update", "retrieve", "destroy"]:
            self.permission_classes = (IsOwner | IsStaff,)
        return super().get_permissions()


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    # serializer_class = HabitSerializer
    pagination_class = MaterialSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_staff:
            return queryset
        return queryset.filter(owner=user)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action in ["list", "create", "update", "retrieve", "destroy"]:
            self.permission_classes = (IsOwner | IsStaff,)
        return super().get_permissions()
