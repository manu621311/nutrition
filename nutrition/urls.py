from django.urls import path
from .views import HomePageView,NutritionHome
urlpatterns=[
          path('',HomePageView.as_view(),name='home'),
          path('nutrition/home',NutritionHome.as_view(),name='nutrition_home'),
          ]
