# Generated by Django 4.2.6 on 2024-03-08 14:15

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_options_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Id')),
                ('user', models.CharField(max_length=100, verbose_name='Username')),
                ('image', models.ImageField(upload_to='post_images', verbose_name='Image')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_likes', models.IntegerField(default=0)),
            ],
        ),
    ]
