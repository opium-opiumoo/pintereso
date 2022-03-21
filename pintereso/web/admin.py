from django.contrib import admin

# Register your models here.
from pintereso.web.models import Profile, Photo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass