from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required

from instagram.forms import InstagramImageForm
from .models import Image,Stream

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    images= Stream.objects.filter(user=user)  #get all stream objects created by user

    groups_ids= [] #create empty dict

    for image in images:
        groups_ids.append(image.image_id)
    
    image_items = Image.objects.all().order_by('-post_date') #selecting
        
    return render(request,'index.html',{'image_items':image_items})

@login_required(login_url='/accounts/login/')
def ImageDetails(request,image_id):
    image = get_object_or_404(Image, id=image_id)

    return render(request,'post_detail.html',{'image':image})


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