from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import make_password

from pintereso.web.models import Profile

UserModel = get_user_model()

class CreateProfileForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(user=user)

        if commit:
            profile.save()
        return user


    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', )

class UpdateProfileForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        required=False,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        required=False,
    )

    profile_pic = forms.ImageField(
        required=False,
    )

    profile_cover = forms.ImageField(
        required=False,
    )

    date_of_birth = forms.DateField(
        required=False,
    )

    description = forms.CharField(
        widget=forms.Textarea,
    )

    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
        required=False,
    )

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
        first_name=self.cleaned_data['first_name'],
        last_name=self.cleaned_data['last_name'],
        profile_pic=self.cleaned_data['profile_pic'],
        profile_cover=self.cleaned_data['profile_cover'],
        date_of_birth=self.cleaned_data['date_of_birth'],
        gender=self.cleaned_data['gender'],
        description=self.cleaned_data['description'],
        user=user)

        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ("first_name", "last_name", "profile_pic", "profile_cover", "date_of_birth", "description", "gender", )