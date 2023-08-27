from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    """ Класс для работы с продуктами (CRUD). """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Поиск продукта по названию/описанию:
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    """ Класс для работы со складами. (CRUD). """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # Поиск склада по конкретному продукту:
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']