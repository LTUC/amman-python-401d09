from django.urls import path

from .views import ThingListView, ThingDetailView

urlpatterns = [
    path('', ThingListView.as_view(), name = 'things_list'),
    path('<int:pk>/', ThingDetailView.as_view(), name = 'things_detail'),
]