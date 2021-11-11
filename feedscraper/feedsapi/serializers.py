from rest_framework import serializers

from .models import Feed


class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        fields = ("id", "guid", "title", "description",
                  "link", "published", "tag")

    def __str__(self):
        return self.title
