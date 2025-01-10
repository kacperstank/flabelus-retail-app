from rest_framework import serializers
from .models import (
    Role, User, Region, Store, UserStore, Category, Product,
    ShoeDetail, EarringDetail, ShoeStock, EarringStock, Tag,
    ProductTag, Sale, SaleItem
)


class RoleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Role model.
    """
    class Meta:
        model = Role
        fields = "__all__"  # Include all fields


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = "__all__"  # Include all fields


class RegionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Region model.
    """
    class Meta:
        model = Region
        fields = "__all__"  # Include all fields


class StoreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Store model.
    """
    class Meta:
        model = Store
        fields = "__all__"  # Include all fields


class UserStoreSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserStore model.
    """
    class Meta:
        model = UserStore
        fields = "__all__"  # Include all fields


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = "__all__"  # Include all fields


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """
    class Meta:
        model = Product
        fields = "__all__"  # Include all fields


class ShoeDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the ShoeDetail model.
    """
    class Meta:
        model = ShoeDetail
        fields = "__all__"  # Include all fields


class EarringDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the EarringDetail model.
    """
    class Meta:
        model = EarringDetail
        fields = "__all__"  # Include all fields


class ShoeStockSerializer(serializers.ModelSerializer):
    """
    Serializer for the ShoeStock model.
    """
    class Meta:
        model = ShoeStock
        fields = "__all__"  # Include all fields


class EarringStockSerializer(serializers.ModelSerializer):
    """
    Serializer for the EarringStock model.
    """
    class Meta:
        model = EarringStock
        fields = "__all__"  # Include all fields


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tag model.
    """
    class Meta:
        model = Tag
        fields = "__all__"  # Include all fields


class ProductTagSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductTag model.
    """
    class Meta:
        model = ProductTag
        fields = "__all__"  # Include all fields


class SaleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Sale model.
    """
    class Meta:
        model = Sale
        fields = "__all__"  # Include all fields


class SaleItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the SaleItem model.
    """
    class Meta:
        model = SaleItem
        fields = "__all__"  # Include all fields