from django.urls import path
from rest_framework.routers import DefaultRouter

from application.apps import ApplicationConfig
from application.views import ChapterViewSet, MaterialViewSet, SubscriptionCreateAPIView, AnswerViewSet, QuestionViewSet

app_name = ApplicationConfig.name

chapter_router = DefaultRouter()
chapter_router.register(r"chapter", ChapterViewSet, basename="chapter")

material_router = DefaultRouter()
material_router.register(r"material", MaterialViewSet, basename="material")

question_router = DefaultRouter()
question_router.register(r"question", QuestionViewSet, basename="question")

answer_router = DefaultRouter()
answer_router.register(r"answer", AnswerViewSet, basename="answer")

urlpatterns = [
    path("subscription/create", SubscriptionCreateAPIView.as_view(), name="create_subscription"),
] + chapter_router.urls + material_router.urls + question_router.urls + answer_router.urls
# urlpatterns.extend(material_router.urls)
