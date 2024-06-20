from django.contrib import admin

from application.models import Chapter, Material, Subscription


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


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("chapter", "subscriber", )
