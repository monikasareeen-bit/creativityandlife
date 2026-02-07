from django.contrib import admin
from .models import Category, Video, OnlineClass, Enquiry

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']

@admin.register(OnlineClass)
class OnlineClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'is_available']
    list_filter = ['category', 'is_available']

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'interested_class', 'created_at']
    list_filter = ['created_at']
    readonly_fields = ['created_at']