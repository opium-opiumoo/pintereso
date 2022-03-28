from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView

from pintereso.accounts.forms import CreateProfileForm, UpdateProfileForm
from pintereso.web.models import Profile, Photo

UserModel = get_user_model()

class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        # save the new user first
        form.save()
        # get the username and password
        email = self.request.POST['email']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'], )
        login(self.request, user)
        return redirect('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

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

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')



class UserProfileView(DetailView):
    model = UserModel
    template_name = 'author.html'
    context_object_name = 'profile'

    def is_user_owner(self):
        user = self.request.user
        current_user = self.request.path.split('/')[-1]
        if int(user.pk) == int(current_user):
            return True
        return False

    def is_user_authenticated(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = list(Photo.objects.filter(user_profile_id=self.object.id))
        total_photos_count = len(photos)
        if self.is_user_owner():
            context['is_owner'] = True
        if self.is_user_authenticated():
            context['is_auth'] = True
        context.update({
            "photos": photos,
            "total_photos_count": total_photos_count,
        })
        return context

class EditUserProfileView(UpdateView):
    model = UserModel
    template_name = 'update-user.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('index')

    def is_user_owner(self):
        user = self.request.user
        current_user = self.request.path.split('/')[-1]
        if int(user.pk) == int(current_user):
            return True
        return False

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.is_user_owner():
            context['is_owner'] = True
        else:
            return redirect('index')
        return context

class ChangeUserPasswordView:
    pass