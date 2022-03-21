from django.urls import path

from pintereso.accounts.views import UserLoginView, UserProfileView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('<int:pk>', UserProfileView.as_view(), name='account'),
)