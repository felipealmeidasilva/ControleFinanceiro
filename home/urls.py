from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastros, name='cadastros'),
]