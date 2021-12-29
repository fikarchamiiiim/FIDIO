from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Video

# Create your views here.
class WatchView(TemplateView):
    template_name = "video/video_page.html"

    def get(self, request, slug, *args, **kwargs):
        video = Video.objects.get(slug=slug)
        
        context = {
            'video' : video,
        }
        return render(request, self.template_name, context)