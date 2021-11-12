from rest_framework import filters, generics

from .models import Feed, StandardResultsSetPagination
from .serializers import FeedSerializer

# Create your views here.


class FeedListAPIView(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["id", "tag", "title"]
    ordering = ["id", "tag", "title"]
    search_fields = ["tag"]
    pagination_class = StandardResultsSetPagination


class FeedDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
