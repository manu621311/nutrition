from rest_framework import serializers
from nutrition.models import Post,Nutrifile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('subject','body','author','date')
        
class NutriSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nutrifile
        fields=['id','name','detail','serving_size','calories','total_fat','protein','cholestrol','carbohydrates','fiber',]
class nutriSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    detail=serializers.CharField(max_length=2000)
    image=serializers.ImageField()
    serving_size=serializers.DecimalField(max_digits=8,decimal_places=1)
    calories=serializers.DecimalField(max_digits=8,decimal_places=1)
    total_fat=serializers.DecimalField(max_digits=8,decimal_places=1)
    protein=serializers.DecimalField(max_digits=8,decimal_places=1)
    cholestrol=serializers.DecimalField(max_digits=8,decimal_places=1)
    carbohydrates=serializers.DecimalField(max_digits=8,decimal_places=1)
    fiber=serializers.DecimalField(max_digits=8,decimal_places=1)