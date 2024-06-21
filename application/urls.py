from django.urls import path
from rest_framework.routers import DefaultRouter

from application.apps import ApplicationConfig
from application.views import ChapterViewSet, MaterialViewSet, SubscriptionCreateAPIView

app_name = ApplicationConfig.name

chapter_router = DefaultRouter()
chapter_router.register(r"chapter", ChapterViewSet, basename="chapter")

material_router = DefaultRouter()
material_router.register(r"material", MaterialViewSet, basename="material")

urlpatterns = (
    [
        path("subscription/create", SubscriptionCreateAPIView.as_view(), name="create_subscription"),
    ]
    + chapter_router.urls
    + material_router.urls
)
