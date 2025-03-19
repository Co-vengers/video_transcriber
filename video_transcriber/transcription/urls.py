from django.urls import path
from .views import register, user_login, user_logout, upload_video, video_list, video_detail

urlpatterns = [
    path('', upload_video, name='upload_video'),
    path('videos/', video_list, name='video_list'),
    path('videos/<int:video_id>/', video_detail, name='video_detail'),

    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
