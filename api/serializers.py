from rest_framework import serializers
from nutrition.models import Post,Nutrifile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('subject','body','author','date')
        
class NutriSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nutrifile
        fields='__all__'