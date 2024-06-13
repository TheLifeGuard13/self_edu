from django.contrib import admin

from application.models import Chapter, Material


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("__all__",)
    search_fields = ('name', )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("__all__", )
    # list_filter = ('category', 'created_at', 'updated_at', )
    # search_fields = ('name', 'last_name', 'category', )

