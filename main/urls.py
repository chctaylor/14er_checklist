from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('mountains/', views.MountainsView, name='mountains'),
    path('climber/<str:pk>', views.ClimberView, name='climber'),
]