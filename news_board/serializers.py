from rest_framework import serializers
from .models import Post, UpVote


class PostSerializer(serializers.ModelSerializer):

    upvotes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "author_name",
            "title",
            "link",
            "upvotes",
            "creation_date",
        )
        extra_kwargs = {
            "creation_date": {"read_only": True},
        }

    def get_upvotes(self, post):
        return UpVote.objects.filter(post=post).count()
