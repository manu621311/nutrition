from rest_framework import generics
from nutrition.models import Post,Nutrifile
from .serializers import PostSerializer,NutriSerializer

# Create your views here.
class PostAPIView(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class NutriAPIView(generics.ListAPIView):
    queryset=Nutrifile.objects.all()
    serializer_class=NutriSerializer
    
class NutriDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Nutrifile.objects.all()
    serializer_class=NutriSerializer