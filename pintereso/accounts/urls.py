from django.urls import path

from pintereso.accounts.views import UserLoginView, UserProfileView, UserRegisterView, EditUserProfileView, \
    UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('<int:pk>', UserProfileView.as_view(), name='account'),
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('update/<int:pk>', EditUserProfileView.as_view(), name='update user'),
    path('logout/', UserLogoutView.as_view(), name="logout user"),
)