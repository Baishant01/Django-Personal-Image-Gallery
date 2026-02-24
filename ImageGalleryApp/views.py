from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ImagePostForm
from django.contrib import messages
from .models import ImagePost
# Create your views here.

def home_view (request):
    return render (request, 'ImageGalleryApp/home.html')
def register_view (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
        else:
            messages.error(request, 'Error while submitting form...')
    else:
        form = RegisterForm()
    return render (request, 'ImageGalleryApp/register.html', {'form':form})

def login_view (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('image_gallery')
        else:
            messages.error(request, 'Invalid login credentials...')
            return redirect ('login')
          
    else:
        return render (request, 'ImageGalleryApp/login.html') 
def logout_view (request):
    logout(request)
    return redirect('home')

@login_required
def image_gallery_view (request):
    images = ImagePost.objects.filter(user=request.user).order_by('id')
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        
        if form.is_valid():
            image_post = form.save(commit=False)
            image_post.user = request.user
            image_post.save()
            return redirect ('image_gallery')
        else:
            messages.error(request, 'Error fetching image...')
    
    else:
        form = ImagePostForm()
    
    context = {
        'form': form,
        'images': images
    }
        
    return render (request, 'ImageGalleryApp/image_gallery.html', context=context)

@login_required
def image_details_view (request, id):
    img_obj = get_object_or_404(ImagePost, id=id, user=request.user)
        
    return render (request, 'ImageGalleryApp/image_details.html', {'img_obj':img_obj})

@login_required
def image_delete_view (request, id):
    img_obj = get_object_or_404(ImagePost, id=id, user=request.user)
    if img_obj.image:
        img_obj.image.delete()
    img_obj.delete()
    return redirect('image_gallery')