from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from taggit.managers import TaggableManager

from pintereso.web.validators import only_letters_validator

# Create your models here.

UserModel = get_user_model()

class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do Not Show'

    GENDERS = [
        (x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)
    ]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
        null=True,
        blank=True,
    )

    profile_pic = models.ImageField(
        validators=(
            # image_max_size_validator,
        ),
        upload_to='images',
        blank=True,
        null=True,
    )

    profile_cover = models.ImageField(
        validators=(
            # image_max_size_validator,
        ),
        upload_to='images',
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Photo(models.Model):
    PHOTO_TITLE_MAX_LENGTH = 50
    PHOTO_TITLE_MIN_LENGTH = 2

    title = models.CharField(
        max_length=PHOTO_TITLE_MAX_LENGTH,
        validators=(
            MinLengthValidator(PHOTO_TITLE_MIN_LENGTH),
        )
    )

    photo = models.ImageField(
        validators=(
            # image_max_size_validator,
        ),
        upload_to='images',
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    tags = TaggableManager()

    user_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )