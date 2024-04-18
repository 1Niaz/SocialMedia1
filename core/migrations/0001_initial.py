# Generated by Django 4.2.6 on 2024-03-07 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='User Id')),
                ('bio', models.TextField(blank=True, verbose_name='User Bio')),
                ('profileimg', models.ImageField(default='blank-profile-picture.png', upload_to='profile_images', verbose_name='User Profile Image')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='User Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
