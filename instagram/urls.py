from django.urls import re_path,path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index, name='indexPage'),
    path('<image_id>',views.ImageDetails, name='imagedetails'), #name matches the reverse
    path('new/image', views.new_image, name='new-image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
