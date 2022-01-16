
from django.urls import path

from .views import index_view, redirect_short_url_view

app_name = 'shortener'

urlpatterns = [
    path('', index_view, name='index'),
    path('<str:shortened_url_part>', redirect_short_url_view, name='redirect')
]