from django.contrib import admin

from application.models import Chapter, Material, Question, Answer, Subscription


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview", "owner", "created", )
    search_fields = ('name', "owner", )
    list_filter = ('owner', 'created', )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview", "owner", "created", )
    search_fields = ('name', "owner", )
    list_filter = ('owner', 'created', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "material", "owner", )
    search_fields = ("owner", )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer", "question", "owner", "is_correct", )
    search_fields = ("owner", )
    list_filter = ("owner", "is_correct", "question", )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("chapter", "subscriber", )

