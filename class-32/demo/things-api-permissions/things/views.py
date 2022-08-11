from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import Thing, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import ThingSerializer, PostSerializer
# Create your views here.

class ThingListView(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class ThingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
