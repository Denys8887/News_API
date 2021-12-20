from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, UpVote
from .serializers import PostSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError


class GenericAPiView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SingleMessageAPiView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class PostUpVoteView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, post_pk):
        try:
            post = Post.objects.get(id=post_pk)
        except Post.DoesNotExist:
            raise Http404
        user = request.user
        try:
            UpVote.objects.create(user=user, post=post)
            return Response({"message": "Post upvoted!"}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(
                {"message": "You've voted before!"}, status=status.HTTP_403_FORBIDDEN
            )
