from django.shortcuts import render
from .models import InstaPost
from django.views.generic import (
    ListView
)
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from .serializers import (
    InstaPostSerializer
)
from rest_framework.permissions import IsAuthenticated, AllowAny

class InstaListView(ListView):
    template_name = 'insta_post_list.html'
    queryset = InstaPost.objects.all
    context_object_name = 'post'

class InstaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = InstaPost.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = InstaPostSerializer

    def create(self, request):
        post = InstaPost.objects.filter(
            name=request.data.get('caption'),
            owner=request.user
        )
        if post:
            msg = 'This post already exists, would you like to post it again?'
            raise ValidationError(msg)
        return super().create(request)
    # user can only delete category he created
    def destroy(self, request, *args, **kwargs):
        post = InstaPost.objects.get(pk=self.kwargs["pk"])
        if not request.user == post.owner:
            raise PermissionDenied("You can not delete this post")
        return super().destroy(request, *args, **kwargs)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
