from django.db import models

# Create your models here.
class Profile(models.Model):
    bio=models.CharField(max_length=50)
    profile_photo=models.ImageField(upload_to='profile/',)

    def __str__(self):
        return self.bio

class Image(models.Model):
    image_name =models.CharField(max_length=50)
    image_caption =models.CharField(max_length=50)
    pic=models.ImageField(upload_to='image/',)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null = True,)
    post_date = models.DateTimeField(auto_now_add=True,blank=True,null = True,)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']

