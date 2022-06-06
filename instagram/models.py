from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save

def user_directory_path(instance, filename):
    #this file will be uploaded to MEDIA_ROOT/user(id/filename)
    return 'user_{0}/{1}'.format(instance.user.id,filename)

# Create your models here.
class Profile(models.Model):
    bio=models.CharField(max_length=50)
    profile_photo=models.ImageField(upload_to='profile/',)

    def __str__(self):
        return self.bio

from tinymce.models import HTMLField
class Image(models.Model):
    
    image_name =models.CharField(max_length=50)
    image_caption =models.CharField(max_length=50)
    pic=models.ImageField(upload_to=user_directory_path,blank=True,null = True)
    post = HTMLField(blank=True,null = True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null = True,)
    post_date = models.DateTimeField(auto_now_add=True,blank=True,null = True,)
    likes = models.IntegerField(blank=True,null = True,)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('imagedetails',args=[str(self.id)])#clickto image get to imagedetails url

    class Meta:
        ordering = ['image_name']
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE,related_name='following')

class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,)
    date =models.DateTimeField()

    def add_image(sender,instance, *args, **kwargs):
        image =instance
        user =image.user
        followers = Follow.objects.all().filter(following=user) #filter all users following me
        for follower in followers:
            stream =Stream(image=image, user=follower.follower,date =image.post_date, following=user)
            stream.save()

post_save.connect(Stream.add_image,sender=Image)


    
