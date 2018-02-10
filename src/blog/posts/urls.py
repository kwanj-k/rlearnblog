from django.urls import path, re_path

from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(),name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<slug:slug>/', PostUpdateView.as_view(), name='post-detail'),
    
    #path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]