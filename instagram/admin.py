from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile,Image

admin.site.register(Image)
admin.site.register(Profile)
