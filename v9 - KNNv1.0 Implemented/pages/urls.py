from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dataset/', views.DatasetPageView.as_view(), name='dataset'),
    path('target_model/', views.TargetPageView.as_view(), name='target_model')
]