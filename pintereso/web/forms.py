from django import forms
from django.contrib.auth import get_user_model
from django.forms.models import (
    inlineformset_factory,
)

from pintereso.web.models import Photo

UserModel = get_user_model()

class CreatePhotoForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        photo = super().save(commit=False)

        photo.user_profile_id = self.user.pk
        if commit:
            photo.save()

        return photo

    class Meta:
        model = Photo
        fields = ('title', 'photo', 'description', )


