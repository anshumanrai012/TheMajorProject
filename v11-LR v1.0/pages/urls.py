from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dataset/', views.DatasetPageView.as_view(), name='dataset'),
    path('target_model/', views.TargetPageView.as_view(), name='target_model'),
    path('about/', views.AboutPageView.as_view(), name='about')
]