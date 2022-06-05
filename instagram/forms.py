from django import forms
from .models import Image

class InstagramImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date']
        widgets = {
            'image_name':forms.TextInput(),
            'image_caption':forms.TextInput(),
           
        }