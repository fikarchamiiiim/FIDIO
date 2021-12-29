from django.urls import path
from .views import WatchView

urlpatterns = [
    path('<str:slug>/', WatchView.as_view(), name='watch_page'),
]