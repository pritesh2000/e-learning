from django.contrib import admin
from LearningApp.models import Contact, Category, Video

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_per_page = 20
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('c_title', 'cat', 'c_id', 'c_image')
    list_per_page = 20
    search_fields = ('c_title',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('v_title', 'v_cat', 'v_id', 'v_image')
    list_per_page = 20
    list_filter = ('v_cat',)
    search_fields = ('v_title',)

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, VideoAdmin)
