from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from instagram.forms import InstagramImageForm
from .email import send_welcome_email

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
   
    
    return render(request,'post_detail.html')

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = InstagramImageForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('indexPage')

    else:
        form = InstagramImageForm()
        
    return render(request, 'new_image.html', {"form": form})