from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView

from pintereso.web.forms import CreatePhotoForm
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
        if self.is_user_authenticated():
            context['is_auth'] = True
        return context

class CreatePhotoView(CreateView, LoginRequiredMixin):
    model = Photo
    form_class = CreatePhotoForm
    template_name = 'new_post.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        return reverse("photo", kwargs={'pk': self.object.pk})

class PhotoDetailsView(DetailView):
    model = Photo
    template_name = "post.html"


    def is_user_authenticated(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        if self.is_user_authenticated():
            context['is_auth'] = True
        context.update({
            "photo": photo,
        })
        return context