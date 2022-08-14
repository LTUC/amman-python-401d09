from django.urls import path

from .views import ThingListCreateView, ThingDetailView
urlpatterns = [
    path('', ThingListCreateView.as_view(), name='thing_list_create'),
    path('<int:pk>/', ThingDetailView.as_view(), name='thing_detail'),
]