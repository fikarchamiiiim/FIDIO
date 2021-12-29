from django.shortcuts import render
from django.views.generic import TemplateView
from video_app.models import Video

# Create your views here.
class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        videos = Video.objects.all()

        context = {
            'videos': videos
        }
        return render(request, self.template_name, context)
