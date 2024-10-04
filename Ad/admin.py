from django.contrib import admin
from .models import Category, Ad


class AdAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    list_display_links = ('id','title')
    search_fields = ('id', 'title', 'content')
    list_filter = ('category', 'added', )
   
admin.site.register(Category)
admin.site.register(Ad, AdAdmin)

