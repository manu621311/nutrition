from django.urls import path
from .views import PostAPIView,NutriAPIView,NutriDetail
urlpatterns=[
      path('community/',PostAPIView.as_view()),
      path('nutrifile/',NutriAPIView.as_view()),
      path('nutrifile/<int:pk>/',NutriDetail.as_view()),
      ]
