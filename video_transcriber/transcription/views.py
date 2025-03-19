from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from .models import Video
from .utils import transcribe_video

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            video.transcript = transcribe_video(video.file.path)
            video.save()
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    
    return render(request, 'upload.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})
