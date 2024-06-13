# from rest_framework import generics, viewsets
#
# from habbits.models import Habit
# from habbits.paginators import HabitPaginator
# from habbits.serializers import HabitSerializer
#
# from users.permissions import IsOwner, IsStaff
#
# class HabitViewSet(viewsets.ModelViewSet):
#     queryset = Habit.objects.all()
#     serializer_class = HabitSerializer
#     pagination_class = HabitPaginator
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         user = self.request.user
#         if user.is_staff:
#             return queryset
#         return queryset.filter(owner=user)
#
#     def perform_create(self, serializer):
#         habit = serializer.save()
#         habit.owner = self.request.user
#         habit.save()
#
#
#     def get_permissions(self):
#         if self.action in ["list", "create", "update", "retrieve", "destroy"]:
#             self.permission_classes = (IsOwner | IsStaff,)
#         return super().get_permissions()
