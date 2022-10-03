from django.shortcuts import render
from django_rest.api.models import Product, Category
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics as api_view
from rest_framework import mixins as api_mixins


# Create your views here.


# serializers.py

class CategoryForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer()

    # category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Product
        fields = "__all__"


class ProductsListView(APIView):
    http_method_names = ("get", "post")

    @staticmethod
    def get(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(data=serializer.data)

    @staticmethod
    def post(request):
        serializer = ProductSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
            return Response(status=201)
        return Response(serializer.errors, status=400)


# class SecondGenericsProductsListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
class SecondGenericsProductsListView(api_view.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SingleProductView(api_view.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomView(api_view.ListAPIView, api_mixins.DestroyModelMixin):
    pass
