# Generated by Django 3.2 on 2021-12-28 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=16)),
                ('address', models.TextField()),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=16)),
                ('status', models.BooleanField(default=True)),
                ('profile_picture', models.ImageField(blank=True, default='-', upload_to='media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
