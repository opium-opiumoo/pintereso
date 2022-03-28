from django.urls import path

from pintereso.web.views import IndexView, CreatePhotoView, PhotoDetailsView, PhotoDeleteView, PhotoEditView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('photo/add/', CreatePhotoView.as_view(), name='create photo'),
    path('photo/<int:pk>', PhotoDetailsView.as_view(), name='photo details'),
    path('photo/edit/<int:pk>', PhotoEditView.as_view(), name='photo edit'),
    path('photo/delete/<int:pk>', PhotoDeleteView.as_view(), name='photo delete'),
)