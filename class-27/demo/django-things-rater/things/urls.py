from django.urls import path

from .views import HomePage, ThingsListView, ThingsDetailView
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('things/', ThingsListView.as_view(), name="things_list"),
    path('things/<int:pk>/', ThingsDetailView.as_view(), name = 'thing_detail')
]
