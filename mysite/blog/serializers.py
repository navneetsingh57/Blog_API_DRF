from rest_framework import serializers
from .models import Post,Comment


class CommentSerializer(serializers.ModelSerializer):
    
    commentor = serializers.StringRelatedField(read_only=True)
    
    class Meta():
        model = Comment
        exclude = ['post']
        read_only_fields = ['id','post']

class PostSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Post
        exclude = ['reported','created_on']
        read_only_fields = ['id']
      
    author = serializers.StringRelatedField(read_only=True)
    post_comments = serializers.StringRelatedField(many=True,read_only=True)
    
        