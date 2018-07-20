from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreditListView.as_view(), name='credit_list'),
    path('<int:pk>/edit/',views.CreditUpdateView.as_view(), name='credit_edit'),
    path('<int:pk>/', views.CreditDetailView.as_view(), name='credit_detail'),
    path('<int:pk>/delete/', views.CreditDeleteView.as_view(), name='credit_delete'),
    path('new/', views.CreditCreateView.as_view(), name='credit_new'),

    path('profile/', views.PersonalListView.as_view(), name='personal_list'),
    path('profile/<int:pk>/edit/',views.PersonalUpdateView.as_view(), name='personal_edit'),
    path('profile/<int:pk>/', views.PersonalDetailView.as_view(), name='personal_detail'),
    path('profile/new/', views.PersonalCreateView.as_view(), name='personal_new'),

    path('profile/predict', views.prediction, name='predict')




]