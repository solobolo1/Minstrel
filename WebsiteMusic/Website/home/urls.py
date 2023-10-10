from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
    , path('main1/', views.main1, name='main1')
    , path('main2/', views.main2, name='main2')
    , path('save-text/', views.save_text, name='save_text')
]