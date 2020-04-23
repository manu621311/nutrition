from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post,Nutrifile
from django.http import HttpResponse,JsonResponse
# Create your views here.
class HomePageView(TemplateView):
      template_name='home.html'
      
class NutritionHome(TemplateView):
      template_name='nutrition_home.html'
      
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='post_new.html'
    fields=('subject','body')
    login_url='login'
    def form_valid(self,form):
         form.instance.author=self.request.user
         return super().form_valid(form)
class PostEditView(LoginRequiredMixin,UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=('subject','body')
    login_url='login'
    def dispatch(self,request,*args,**kwargs):
        obj=self.get_object()
        if obj.author!=self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)   
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('post_list')
    login_url='login'
    def dispatch(self,request,*args,**kwargs):
        obj=self.get_object()
        if obj.author!=self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)
class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'
class PostListView(ListView):
    model=Post
    template_name='post_list.html'
    
class NutriFile(ListView):
    context_object_name='items'
    model=Nutrifile
    template_name='nutrifile.html'
    """def respond_data(self,request):
        x=request.GET.get('search_text')
        if x:
            return HttpResponse('dk')
        else:
            return None"""

def Filtered(request):
    x=request.GET.get('search_text')
    #return JsonResponse({"dk":)
    if x:
        return JsonResponse({'dk':x})
    else:
        return None