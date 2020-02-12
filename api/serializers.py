from rest_framework import serializers
from nutrition.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('subject','body','author','date')
