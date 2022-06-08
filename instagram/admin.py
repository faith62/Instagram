# Register your models here.
from django.contrib import admin
from .models import Follow, Profile,Image, Stream

class ImageAdmin(admin.ModelAdmin):    
   
    list_display = ('user','image_name', 'pic')

admin.site.register(Image, ImageAdmin)
admin.site.register(Profile)
admin.site.register(Stream)
admin.site.register(Follow)
