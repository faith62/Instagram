from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from instagram.forms import InstagramImageForm
from .models import Image,Stream

# Create your views here.


def index(request):
    user = request.user
    images= Stream.objects.filter(user=user)  #get all stream objects created by user

    groups_ids= [] #create empty dict

    for image in images:
        groups_ids.append(image.image_id)
    
    image_items = Image.objects.filter(id_in = groups_ids).all().order_by('-post_date') #selecting
        
    return render(request,'index.html',{'image_items':image_items})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = InstagramImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('indexPage')

    else:
        form = InstagramImageForm()
        
    return render(request, 'new_image.html', {"form": form})