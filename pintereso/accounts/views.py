from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView

from pintereso.web.models import Profile, Photo


class UserRegisterView:
    pass

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)



class UserProfileView(DetailView):
    model = Profile
    template_name = 'author.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = list(Photo.objects.filter(user_profile_id=self.object.user_id))
        total_photos_count = len(photos)
        context.update({
            "photos": photos,
            "total_photos_count": total_photos_count,
        })
        return context

class EditUserProfileView:
    pass

class ChangeUserPasswordView:
    pass