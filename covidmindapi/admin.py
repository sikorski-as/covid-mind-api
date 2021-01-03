from django.contrib import admin
from .models import Activity, Category


# Register your models here.

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'description', 'link', 'categories_', 'visible')

    def categories_(self, obj):
        return ', '.join(category.name for category in obj.categories.all())


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
