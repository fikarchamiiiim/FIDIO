import uuid
from django.db import models
from django.contrib.auth.models import User
from video_app.models import Video

# Create your models here.
class UserProfile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=16)
    address = models.TextField()
    birth_date = models.DateField()
    phone = models.CharField(max_length=16)
    status = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='media', default='-', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.user.username)