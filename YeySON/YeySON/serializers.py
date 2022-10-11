from rest_framework import serializers
from YeySON.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'date', 'content')