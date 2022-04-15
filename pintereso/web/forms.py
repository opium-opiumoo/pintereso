from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from crispy_forms.helper import FormHelper

from pintereso.web.models import Photo

UserModel = get_user_model()

class CreatePhotoForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        form = CreatePhotoForm
        photo = super().save(commit=False)

        photo.user_profile_id = self.user.pk
        if commit:
            photo.save()
            form._save_m2m(self)

        return photo


    class Meta:
        model = Photo
        fields = ('title', 'photo', 'description', 'tags', )

class EditPhotoForm(forms.ModelForm):
    title = forms.CharField(
        max_length=Photo.PHOTO_TITLE_MAX_LENGTH,
        validators=(
            MinLengthValidator(Photo.PHOTO_TITLE_MIN_LENGTH),
        ),
        required=False,
    )

    photo = forms.ImageField(
        required=False,
    )

    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        form = EditPhotoForm
        photo = super().save(commit=False)

        photo.user_profile_id = self.user.pk
        if commit:
            photo.save()
            form._save_m2m(self)

        return photo

    class Meta:
        model = Photo
        fields = ('title', 'photo', 'description', 'tags',)
