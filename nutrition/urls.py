
from django.urls import path
from .views import HomePageView,NutritionHome,PostDetailView,PostDeleteView,PostCreateView,PostEditView,PostListView,NutriFile,Filtered
urlpatterns=[
          path('',HomePageView.as_view(),name='home'),
          path('nutrition/home/',NutritionHome.as_view(),name='nutrition_home'),
          path('nutrition/community/post/list/',PostListView.as_view(),name='post_list'),
          path('nutrition/community/post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
          path('nutrition/community/post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),
          path('nutrition/community/posts/',PostListView.as_view(),name='post_list'),
          path('nutrition/community/<int:pk>/edit/',PostEditView.as_view(),name='post_edit'),
          path('nutrition/nutrifile/',NutriFile.as_view(),name='nutrifile'),
          path('request/',Filtered, name='filter'),
          ]
