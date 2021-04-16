from django.urls import path

from .views import IndexView, SobreView, GenerosView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('generos/', GenerosView.as_view(), name='generos'),
]
