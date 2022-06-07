import profile
from django.urls import reverse
from distutils.log import error
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from instagram.forms import EditProfileForm, InstagramImageForm
from .models import Follow, Image, Likes, Profile,Stream
from django.urls import resolve #help identify url name

# Create your views here.
def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name= resolve(request.path).url_name

    if url_name == "profile":
        images = Image.objects.filter(user=user).order_by('-post_date')
    else:
        images = profile.favorites.all()


    #Profile info stats
    image_count = Image.objects.filter(user = user).count()
    following_count=Follow.objects.filter(follower=user).count()
    followers_count=Follow.objects.filter(following=user).count()

    #Paginator
    paginator = Paginator(images,8)
    page_number = request.GET.get('page')
    images_paginator= paginator.get_page(page_number)

    return render(request,'profile.html',{'images':images_paginator, 'profile':profile, 'url_name':url_name,'image_count':image_count,'following_count':following_count,'followers_count':followers_count})


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

@login_required(login_url='/accounts/login/')
def like(request, image_id):
    user = request.user
    image = Image.objects.get(id = image_id)
    current_likes = image.likes

    liked = Likes.objects.filter(user = user, image = image).count()

    if not liked:
        like = Likes.objects.create(user = user, image = image)      
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user = user, image = image).delete()
        current_likes =current_likes -1

    image.likes = current_likes
    image.save()

    return HttpResponseRedirect(reverse('imagedetails',args=[image.id]))


@login_required(login_url='/accounts/login/')
def EditProfile(request):
	user = request.user.id
	profile = Profile.objects.get(user__id=user)
	BASE_WIDTH = 400

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.profile_photo = form.cleaned_data.get('profile_photo')
			profile.first_name = form.cleaned_data.get('first_name')
			profile.last_name = form.cleaned_data.get('last_name')			
			profile.url = form.cleaned_data.get('url')
			profile.bio = form.cleaned_data.get('bio')
			profile.save()
			return redirect('indexPage')
	else:
		form = EditProfileForm()

	
	return render(request, 'edit_profile.html', {'form':form,})
