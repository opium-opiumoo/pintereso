from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView, DeleteView, UpdateView
from taggit.models import Tag

from pintereso.web.forms import CreatePhotoForm, EditPhotoForm
from pintereso.web.models import Photo

UserModel = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'

    def is_user_authenticated(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = list(Photo.objects.all())
        if self.is_user_authenticated():
            context['is_auth'] = True
        context['photos'] = photos
        return context

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    photos = Photo.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'photos':photos,
    }
    return render(request, 'index.html', context)

class CreatePhotoView(CreateView, LoginRequiredMixin):
    model = Photo
    form_class = CreatePhotoForm
    template_name = 'new_post.html'

    def is_user_authenticated(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        return reverse("photo details", kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.is_user_authenticated():
            context['is_auth'] = True
        return context

class PhotoDetailsView(DetailView):
    model = Photo
    template_name = "post.html"

    def is_user_post(self, **kwargs):
        user_pk = self.request.user.pk
        photo = Photo.objects.get(pk=self.kwargs['pk'])

        if photo.user_profile_id == user_pk:
            return True
        return False

    def is_user_authenticated(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        if self.is_user_authenticated():
            context['is_auth'] = True
        if self.is_user_post():
            context['user_post'] = True
        context.update({
            "photo": photo,
        })
        return context

class PhotoEditView(UpdateView):
    model = Photo
    form_class = EditPhotoForm
    template_name = "edit_post.html"

    def is_user_post(self, **kwargs):
        user_pk = self.request.user.pk
        photo = Photo.objects.get(pk=self.kwargs['pk'])

        if photo.user_profile_id == user_pk:
            return True
        return False

    def is_user_authenticated(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        if self.is_user_authenticated():
            context['is_auth'] = True
        if self.is_user_post():
            context['user_post'] = True
        context.update({
            "photo": photo,
        })
        return context

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        return reverse("photo details", kwargs={'pk': self.object.pk})

class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = "photo_delete.html"

    def is_user_post(self, **kwargs):
        user_pk = self.request.user.pk
        photo = Photo.objects.get(pk=self.kwargs['pk'])

        if photo.user_profile_id == user_pk:
            return True
        return False

    def is_user_authenticated(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        if self.is_user_authenticated():
            context['is_auth'] = True
        if self.is_user_post():
            context['user_post'] = True
        context.update({
            "photo": photo,
        })
        return context

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        return reverse("account", kwargs={'pk': self.request.user.pk})