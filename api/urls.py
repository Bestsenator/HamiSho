from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-main'),
    path('getCandidateInfo/', views.getCandidateInfo),
    path('getPostCandidate/', views.getPostCandidate),
    path('getNewsCandidate/', views.getNewsCandidate),
    path('setSupporter/', views.setSupporter),
    path('setMessageToCandidate/', views.setMessageToCandidate),
    path('getDeveloperInfo/', views.getDeveloperInfo),
    path('getSocialCandidate/', views.getSocialCandidate),
]
