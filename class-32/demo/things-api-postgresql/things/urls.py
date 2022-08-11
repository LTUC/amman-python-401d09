from django.urls import path

from .views import ThingListView, ThingDetailView, PostListView, PostDetailView
urlpatterns = [
    path('', ThingListView.as_view(), name= 'thing_list'),
    path('<int:pk>/', ThingDetailView.as_view(), name= 'thing_detail'),
    path('post/', PostListView.as_view(), name= 'post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post_detail'),
]
