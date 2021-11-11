from django.db import models
from rest_framework.pagination import PageNumberPagination

# Create your models here.


class Feed(models.Model):
    description = models.CharField(max_length=3000)
    title = models.CharField(max_length=500)
    guid = models.CharField(max_length=5255)
    link = models.CharField(max_length=255)
    published = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'pageSize'
    max_page_size = 100
