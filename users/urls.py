from django.urls import path
from .views import SignUpView,AccountSettingsView

urlpatterns=[
              path('signup/',SignUpView.as_view(),name='sign_up'),
              path('settings/',AccountSettingsView.as_view(),name='account_settings'),
            ]
