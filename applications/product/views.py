from django.db.models import Q
from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from applications.product.filters import ProductFilter
from applications.product.models import Product
from applications.product.permissions import IsAdmin, IsAutor
from applications.product.serializers import ProductSerializer

class LargeResultsSetPagination(PageNumberPagination):
    page_size =3
    page_size_query_param = 'page_size'
    max_page_size = 100
class ListCreateView(ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_fields = ['category','price']
    # filter_class = ProductFilter
    search_fields = ['name','description']
    ordering_fields = ['id']


    def qet_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        if search:
            queryset=queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return queryset
class DeleteUpdateRetriveView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes =[IsAuthenticated]
    # pagination_class = LargeResultsSetPagination
    permission_classes = [IsAutor]




