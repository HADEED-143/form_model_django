from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('cv/', views.form_view, name='cvpost')
]