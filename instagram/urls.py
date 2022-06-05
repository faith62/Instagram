from django.urls import re_path,path
from . import views

urlpatterns=[
    path('',views.index, name='indexPage'),
    path('new/image', views.new_image, name='new-image')
]