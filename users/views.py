from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
# Create your views here.

class SignUpView(CreateView):
     form_class=CustomUserCreationForm
     success_url=reverse_lazy('login')
     template_name='signup.html'
     
class AccountSettingsView(TemplateView):
     template_name='account_settings.html'