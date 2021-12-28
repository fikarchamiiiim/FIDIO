from django.contrib import admin
from .models import Video, VideoLike, VideoDislike

# Register your models here.
admin.site.register(Video)
admin.site.register(VideoLike)
admin.site.register(VideoDislike)