from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    RoleViewSet, UserViewSet, RegionViewSet, StoreViewSet,
    UserStoreViewSet, CategoryViewSet, ProductViewSet,
    ShoeDetailViewSet, EarringDetailViewSet, ShoeStockViewSet,
    EarringStockViewSet, TagViewSet, ProductTagViewSet,
    SaleViewSet, SaleItemViewSet
)

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'users', UserViewSet, basename='user')
router.register(r'regions', RegionViewSet, basename='region')
router.register(r'stores', StoreViewSet, basename='store')
router.register(r'user-stores', UserStoreViewSet, basename='userstore')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'shoe-details', ShoeDetailViewSet, basename='shoedetail')
router.register(r'earring-details', EarringDetailViewSet, basename='earringdetail')
router.register(r'shoe-stock', ShoeStockViewSet, basename='shoestock')
router.register(r'earring-stock', EarringStockViewSet, basename='earringstock')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'product-tags', ProductTagViewSet, basename='producttag')
router.register(r'sales', SaleViewSet, basename='sale')
router.register(r'sale-items', SaleItemViewSet, basename='saleitem')

urlpatterns = router.urls