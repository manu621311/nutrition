from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post,Nutrifile
from django.http import HttpResponse,JsonResponse
from api.serializers import NutriSerializer,nutriSerializer
from rest_framework.renderers import JSONRenderer
import json
# Create your views here.

def objectserializer():
    l=list()
    for i in queryset1:
        item=nutriSerializer(i)
        l.append(item.data)
    return l
queryset1=Nutrifile.objects.all()
serializerdata=objectserializer()#nutriSerializer(queryset1,many=True)
#items=serializerdata.data
#json=JSONRenderer().render(items)



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
    

def Filtered(request):
    x=request.GET.get('search_text')
    if x:
        for every_record in serializerdata:
            if(x==every_record['name']):
                req_item=every_record
                return HttpResponse(json.dumps(every_record))
        else:
            return None
    
