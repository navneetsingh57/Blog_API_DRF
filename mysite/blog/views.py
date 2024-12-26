from django.shortcuts import render
from .models import Post,Comment
from . import serializers
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .permissions import IsAuthorOrReadOnly, IsCommentorOrReadOnly
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.
        
class PostsList(generics.ListAPIView):
    
    queryset = Post.objects.filter(reported=False)
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class PostCreate(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.all()
    
    def perform_create(self, serializer):

        author = self.request.user
        serializer.save(author=author)
        
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentList(generics.ListAPIView):
    
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(post=pk,report=1)
    

class CommentCreate(generics.CreateAPIView):
    
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        commentor = self.request.user
        if serializer.validated_data['report'] == 1:    
            serializer.save(post=post, commentor=commentor)
        else:
            post.reported = True
            post.save()
            serializer.save(post=post)
        
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsCommentorOrReadOnly]
    
        
