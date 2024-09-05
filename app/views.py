from django.shortcuts import render
from rest_framework import generics
from rest_framework import views, status
from app.models import Product_details
from app.serializers import ProductSerializer
from rest_framework.response import Response
from django.db.models import Q




class Product_curd(views.APIView):
    # Here create product
    def post(self ,request , *args ,**kwargs ):
        product_name = request.data.get("product_name")
        description = request.data.get("description")
        price = request.data.get("price")
        inventory_count = request.data.get("inventory_count")
        category = request.data.get("category")
        if not all([product_name,description,price,inventory_count,category]):
            return Response({"message":"Invalid Credential!!", "status":"400" },status=status.HTTP_400_BAD_REQUEST)
        if len(product_name) == 0 or len(product_name) > 25 or len(product_name) < 4 or price <= 0 or inventory_count < 0 or len(category) == 0 or len(description) > 100 or len(description) < 4 or len(description) > 25 or len(description) < 4:
            return Response({"message": "Invalid Credential!!", "status": "400"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            if Product_details.objects.filter(name= product_name):
                return Response({"message":"Same name product already created !!", "status":"400" },status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"data":None,"message":"Invalid Credential!!", "status":"400" },status=status.HTTP_400_BAD_REQUEST)
        product_data = {"name": product_name,"description": description,"price": price,"inventory_count": inventory_count,"category": category}
        serializer = ProductSerializer(data=product_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Read product
    def get(self, request, *args, **kwargs):
        products = Product_details.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # Update product
    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        try:
            product = Product_details.objects.get(id=id)
        except Product_details.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product_name = request.data.get("product_name")
        description = request.data.get("description")
        price = request.data.get("price")
        inventory_count = request.data.get("inventory_count")
        category = request.data.get("category")

        if len(product_name) == 0 or len(product_name) > 25 or len(product_name) < 4 or price <= 0 or inventory_count < 0 or len(category) == 0 or len(description) > 100 or len(description) < 4 or len(description) > 25 or len(description) < 4:
            return Response({"message": "Invalid Credential!!", "status": "400"}, status=status.HTTP_400_BAD_REQUEST)
        product_data = {
            "name": product_name,
            "description": description,
            "price": price,
            "inventory_count": inventory_count ,
            "category": category
        }

        serializer = ProductSerializer(product, data=product_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete product
    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        try:
            product = Product_details.objects.get(id=product_id)
        except Product_details.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




class ProductSearch(views.APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        if query:
            products = Product_details.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__icontains=query)
            )
        else:
            products = Product_details.objects.all()
        
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductPopularityHighToLowList(views.APIView):
    #poularity high to low 
    def get(self, request, *args, **kwargs):
        products = Product_details.objects.all().order_by('-popularity_score')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductPopularityLowToHighList(views.APIView):
    #poularity low to High
    def get(self, request, *args, **kwargs):
        products = Product_details.objects.all().order_by('popularity_score')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class ProductBuy(views.APIView):
    #product buy 
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        quantity = request.data.get("product_quantity")

        if not all([id, quantity]):
            return Response({"message": "Invalid Credential!!", "status": "400"}, status=status.HTTP_400_BAD_REQUEST)

        if id == 0  or quantity <= 0:
            return Response({"message": "Invalid Credential!!", "status": "400"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product_details.objects.get(id=id)
        except Product_details.DoesNotExist:
            return Response({"message": "Product not found!!", "status": "404"}, status=status.HTTP_404_NOT_FOUND)

        if product.inventory_count < quantity:
            return Response({"message": "Insufficient inventory!!", "status": "400"}, status=status.HTTP_400_BAD_REQUEST)

        product.UpdateInventory(quantity)
        product.update_popularity(quantity)

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)