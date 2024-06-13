# from django.urls import path
# from rest_framework.routers import DefaultRouter
#
# from application.apps import ApplicationConfig
# from application.views import HabitListAPIView, HabitViewSet
#
# app_name = ApplicationConfig.name
#
# router = DefaultRouter()
# router.register(r"habbits", HabitViewSet, basename="habbits")
#
# urlpatterns = [
#     path("public/", HabitListAPIView.as_view(), name="public_habits_list"),
# ] + router.urls