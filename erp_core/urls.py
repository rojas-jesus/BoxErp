from django.urls import path
from .views import (
    panel_main_view,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    client_detail_view,
    SaleCreateView,
    SaleListView,
    sale_detail_view,
    sale_delete_view,
    AuditListView,
    CategoryDeletedListView,
    CategoryRecoverView,
    ProductDeletedListView,
    ProductRecoverView,
    ClientDeletedListView,
    ClientRecoverView,
    SaleDeletedListView,
    SaleRecoverView,
)

app_name = "erp"

urlpatterns = [
    path("panel/main/", panel_main_view, name="panel-main"),

    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("category/create/", CategoryCreateView.as_view(), name="category-create"),
    path("category/<int:pk>/update/", CategoryUpdateView.as_view(), name="category-update"),
    path("category/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("product/create/", ProductCreateView.as_view(), name="product-create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path("clients/", ClientListView.as_view(), name="client-list"),
    path("client/create/", ClientCreateView.as_view(), name="client-create"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),
    path("client/<int:pk>/", client_detail_view, name="client-detail"),
    path("sales/", SaleListView.as_view(), name="sale-list"),
    path("sale/create/", SaleCreateView, name="sale-create"),
    path("sale/<int:pk>/", sale_detail_view, name="sale-detail"),
    path("sale/<int:pk>/delete/", sale_delete_view, name="sale-delete"),

    path("audit/", AuditListView.as_view(), name="audit-list",),
    path("categories-deleted/", CategoryDeletedListView.as_view(), name="category-deleted-list"),
    path("category/<int:id>/recover/", CategoryRecoverView.as_view(), name="category-recover"),
    path("products-deleted/", ProductDeletedListView.as_view(), name="product-deleted-list"),
    path("product/<int:id>/recover/", ProductRecoverView.as_view(), name="product-recover"),
    path("clients-deleted/", ClientDeletedListView.as_view(), name="client-deleted-list"),
    path("client/<int:id>/recover/", ClientRecoverView.as_view(), name="client-recover"),
    path("sales-deleted/", SaleDeletedListView.as_view(), name="sale-deleted-list",),
    path("sale/<int:id>/recover/", SaleRecoverView.as_view(), name="sale-recover",),
]