from rest_framework import serializers
from ..models import Product,Category,User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','category','price','discount','description','status')


    



























# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id','email','full_name')


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     total_price = serializers.SerializerMethodField()
#     category = CategorySerializer()
#     wishlist = UserSerializer(many=True)
#     class Meta:
#         model = Product
#         fields = '__all__'

#     def get_total_price(self,obj):
#         return obj.price - (obj.discount or 0)


# class ProductCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Product
#         fields =(
#             'name','category','price','discount','description','status'
#         )