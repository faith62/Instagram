# Register your models here.
from django.contrib import admin
from .models import Follow, Profile,Image, Stream


admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Stream)
admin.site.register(Follow)
