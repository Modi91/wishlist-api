from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.models import Item
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from .permissions import IsOwner
from .serializers import ItemListSerializer, ItemDetailSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    permission_classes = [AllowAny,]
    filter_backends = [OrderingFilter, SearchFilter,]
    search_fields = ['id','name', 'description',]
    serializer_class = ItemListSerializer


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_feild = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsOwner,]