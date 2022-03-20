from django.urls import path

from pintereso.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)