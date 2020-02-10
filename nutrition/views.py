from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
      template_name='home.html'
      
class NutritionHome(TemplateView):
      template_name='nutrition_home.html'