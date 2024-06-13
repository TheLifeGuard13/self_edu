from django.urls import path
from rest_framework.routers import DefaultRouter

from application.apps import ApplicationConfig
from application.views import ChapterViewSet, MaterialViewSet

app_name = ApplicationConfig.name

chapter_router = DefaultRouter()
chapter_router.register(r"chapter", ChapterViewSet, basename="chapter")

material_router = DefaultRouter()
material_router.register(r"material", MaterialViewSet, basename="material")

urlpatterns = [
    # path("public/", HabitListAPIView.as_view(), name="public_habits_list"),
] + chapter_router.urls
urlpatterns.extend(material_router.urls)
