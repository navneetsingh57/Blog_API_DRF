from django.urls import path
from . import views

urlpatterns = [
    path('post-create/', views.PostCreate.as_view(),name="post-create" ),
    path('list/', views.PostsList.as_view(),name="posts" ),
    path('list/<int:pk>/',views.PostDetail.as_view(),name="post"),
    path('list/<int:pk>/comment/',views.CommentList.as_view(), name="comments"),
    path('list/<int:pk>/comment-create/',views.CommentCreate.as_view(), name="comment-create"),
    path('comment/<int:pk>/',views.CommentDetail.as_view(),name="comment-detail")
]