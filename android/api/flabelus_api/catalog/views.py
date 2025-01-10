from rest_framework import viewsets
from .models import (
    Role, User, Region, Store, UserStore, Category, Product,
    ShoeDetail, EarringDetail, ShoeStock, EarringStock, Tag,
    ProductTag, Sale, SaleItem
)
from .serializers import (
    RoleSerializer, UserSerializer, RegionSerializer, StoreSerializer,
    UserStoreSerializer, CategorySerializer, ProductSerializer, ShoeDetailSerializer,
    EarringDetailSerializer, ShoeStockSerializer, EarringStockSerializer, TagSerializer,
    ProductTagSerializer, SaleSerializer, SaleItemSerializer
)


class RoleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Role model.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Region model.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Store model.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class UserStoreViewSet(viewsets.ModelViewSet):
    """
    ViewSet for UserStore model.
    """
    queryset = UserStore.objects.all()
    serializer_class = UserStoreSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Category model.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoeDetailViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ShoeDetail model.
    """
    queryset = ShoeDetail.objects.all()
    serializer_class = ShoeDetailSerializer


class EarringDetailViewSet(viewsets.ModelViewSet):
    """
    ViewSet for EarringDetail model.
    """
    queryset = EarringDetail.objects.all()
    serializer_class = EarringDetailSerializer


class ShoeStockViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ShoeStock model.
    """
    queryset = ShoeStock.objects.all()
    serializer_class = ShoeStockSerializer


class EarringStockViewSet(viewsets.ModelViewSet):
    """
    ViewSet for EarringStock model.
    """
    queryset = EarringStock.objects.all()
    serializer_class = EarringStockSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Tag model.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductTagViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ProductTag model.
    """
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer


class SaleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Sale model.
    """
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for SaleItem model.
    """
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer