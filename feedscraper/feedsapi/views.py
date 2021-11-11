from rest_framework import filters, generics

from .models import Feed, StandardResultsSetPagination
from .serializers import FeedSerializer

# Create your views here.


class FeedListAPIView(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["title", "published"]
    ordering = ["title"]
    search_fields = ["title", "published"]
    pagination_class = StandardResultsSetPagination


class FeedDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
