from django.db import models
from datetime import datetime
from safedelete.models import SafeDeleteModel
from safedelete.config import SOFT_DELETE


class Category(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(max_length=90, verbose_name="Name", unique=True)
    description = models.CharField(
        max_length=500, null=True, blank=True, verbose_name="Description"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["id"]


class Product(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(max_length=160, verbose_name="name", unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="product/%Y/%m/%d", null=True, blank=True)
    stock = models.PositiveIntegerField(default=1)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="price")

    def __str__(self):
        return f"{self.name} | ${self.pvp} | {self.stock} ud(s)"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["id"]


class Client(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    identity_card_number = models.CharField(
        max_length=10, unique=True, verbose_name="Identity Card Number"
    )
    first_name = models.CharField(max_length=90, verbose_name="First Name")
    last_name = models.CharField(max_length=90, verbose_name="Last Name")
    phone_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Phone"
    )
    date_of_birth = models.DateField(
        default=datetime.now, verbose_name="Date of Birth"
    )
    address = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="Address"
    )
    extra_information = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Extra Information",
    )

    def __str__(self):
        return f"{self.identity_card_number} | {self.first_name}  {self.last_name}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["id"]


class Sale(SafeDeleteModel): 
    _safedelete_policy = SOFT_DELETE

    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, blank=True, null=True
    ) 
    date = models.DateTimeField(auto_now=True) 
    comment = models.TextField(default="", blank=True, null=True) 
    total = models.FloatField(default=0) 


class SaleDetail(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True
    )
    amount = models.IntegerField(default=1)
