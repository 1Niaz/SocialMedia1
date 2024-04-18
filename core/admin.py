from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.


admin.site.register(Profile)
admin.site.register(LikePost)


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at')

@admin.register(FollowersCount)
class FollowersCountAdmin(admin.ModelAdmin):
    list_display = ('user', 'follower')




# Отображение паролей в хэшированном виде

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'display_password')
#     def display_password(self, obj):
#         return obj.password
#     display_password.short_description = 'Hashed Password'
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)