from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import VideoUploadForm
from .models import Video
from .utils import transcribe_video

### AUTH VIEWS ###
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('upload_video')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('upload_video')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

### VIDEO VIEWS ###
@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            video.user = request.user
            video.save()
            
            #transcribe video
            video.transcript = transcribe_video(video.file.path)
            video.save()
            
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    
    return render(request, 'upload.html', {'form': form})

@login_required
def video_list(request):
    videos = Video.objects.filter(user=request.user)
    return render(request, 'video_list.html', {'videos': videos})

@login_required
def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'video_detail.html', {'video': video})
