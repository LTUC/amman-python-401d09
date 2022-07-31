from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('snack/', SnackListView.as_view(), name='snack_list'),
    path('snack/<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('snack/create/', SnackCreateView.as_view(), name='snack_create'),
    path('snack/<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
    path('snack/<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'),
]
