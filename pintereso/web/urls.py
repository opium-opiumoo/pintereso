from django.urls import path

from pintereso.web.views import IndexView, CreatePhotoView, PhotoDetailsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('photo/add/', CreatePhotoView.as_view(), name='create photo'),
    path('photo/<int:pk>', PhotoDetailsView.as_view(), name='photo details'),
)