from django.contrib import admin
from .models import Category, Checkpoint, Technique, KeyPoint, CommonMistake

class KeyPointInline(admin.TabularInline):
    model = KeyPoint
    extra = 1  # Number of empty key point forms to display

class CommonMistakeInline(admin.TabularInline):
    model = CommonMistake
    extra = 1  # Number of empty common mistake forms to display

@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'belt_level', 'init_checkpoint', 'out_checkpoint')
    list_filter = ('category', 'belt_level', 'init_checkpoint', 'out_checkpoint')
    search_fields = ('name', 'description')
    
    # Add inline forms for key points and common mistakes
    inlines = [
        KeyPointInline,
        CommonMistakeInline
    ]

# Register other models with admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Checkpoint)
class CheckpointAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

# Optional: if you want to register KeyPoint and CommonMistake
@admin.register(KeyPoint)
class KeyPointAdmin(admin.ModelAdmin):
    list_display = ('description', 'technique')
    list_filter = ('technique',)

@admin.register(CommonMistake)
class CommonMistakeAdmin(admin.ModelAdmin):
    list_display = ('description', 'technique')
    list_filter = ('technique',)