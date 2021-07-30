from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser, Follow
from .serializers import FollowSerializer


class ListFollowViewSet(ListAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = FollowSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(following__user=user)


class FollowViewSet(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, author_id):
        author = get_object_or_404(CustomUser, id=author_id)
        Follow.objects.get_or_create(user=request.user, author=author)
        serializer = UserSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, author_id):
        author = CustomUser.objects.get(id=author_id)
        try:
            Follow.objects.get(
                user=request.user,
                author=author).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
