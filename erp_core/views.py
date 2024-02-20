from datetime import date 
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView,
    View  
    )
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404, 
    )
from easyaudit.models import CRUDEvent
from .models import (
        Category, 
        Product, 
        Client, 

        Sale, 
        SaleDetail
        )
from .forms import (
    CategoryForm,
    ProductForm,
    ClientForm,
    SaleForm,
    SaleDetailFormSet,
    SaleDetailForm,
)

class AuditListView(LoginRequiredMixin, ListView):
    model = CRUDEvent
    template_name = "erp_core/audit_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Audit"
        return context

class CategoryDeletedListView(LoginRequiredMixin, ListView):
    template_name = "erp_core/category_deleted_list.html"
    context_object_name = "category_deleted_list"

    def get_queryset(self):
        category_deleted_list = Category.all_objects.filter(deleted__isnull=False)
        return category_deleted_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Deleted Categories"
        return context

class CategoryRecoverView(LoginRequiredMixin, View):
    def get(self, request, id):
        category = get_object_or_404(
            Category.all_objects.filter(deleted__isnull=False), id=id
        )
        category.deleted = None
        category.save()
        return redirect(reverse_lazy("erp:category-deleted-list"))


class ProductDeletedListView(LoginRequiredMixin, ListView):
    template_name = "erp_core/product_deleted_list.html"
    context_object_name = "product_deleted_list"

    def get_queryset(self):
        product_deleted_list = Product.all_objects.filter(deleted__isnull=False)
        return product_deleted_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Deleted Products"
        return context

class ProductRecoverView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = get_object_or_404(
            Product.all_objects.filter(deleted__isnull=False), id=id
        )
        product.deleted = None
        product.save()
        return redirect(reverse_lazy("erp:product-deleted-list"))

class ClientDeletedListView(LoginRequiredMixin,ListView):
    template_name = "erp_core/client_deleted_list.html"
    context_object_name = "client_deleted_list"

    def get_queryset(self):
        client_deleted_list = Client.all_objects.filter(deleted__isnull=False)
        return client_deleted_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Deleted Clients"
        return context

class ClientRecoverView(LoginRequiredMixin,View):
    def get(self, request, id):
        client = get_object_or_404(
            Client.all_objects.filter(deleted__isnull=False), id=id
        )
        client.deleted = None
        client.save()
        return redirect(reverse_lazy("erp:client-deleted-list"))


class SaleDeletedListView(LoginRequiredMixin, ListView):
    template_name = "erp_core/sale_deleted_list.html"
    context_object_name = "sale_deleted_list"

    def get_queryset(self):
        sale_deleted_list = Sale.all_objects.filter(deleted__isnull=False)
        return sale_deleted_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Deleted Sales"
        return context


class SaleRecoverView(LoginRequiredMixin,View):
    def get(self, request, id):
        sale = get_object_or_404(
            Sale.all_objects.filter(id=id, deleted__isnull=False)
        )
        sale_detail_list = SaleDetail.all_objects.filter(
            sale__id=id, deleted__isnull=False
        )

        # Recover deleted sales details
        for sale_detail in sale_detail_list:
            sale_detail.deleted = None
            sale_detail.save()

        # Recover the deleted sale
        sale.deleted = None
        sale.save()
        return redirect(reverse_lazy("erp:sale-deleted-list"))


@login_required
def panel_main_view(request):
    if Product.objects.exists():
        quantity_products = Product.objects.count()
    else:
        quantity_products = 0

    if Sale.objects.exists():
        all_sales = Sale.objects.count()
        last_sale = Sale.objects.last()
        last_sale = last_sale.total
        all_sales_current_date = Sale.objects.filter(
            date__gte=date.today()
        ).count()  
    else:
        all_sales = 0
        last_sale = 0
        all_sales_current_date = 0

    title = "Main Panel"

    context = {
        "title": title,
        "quantity_products": quantity_products,
        "all_sales": all_sales,
        "last_sale": last_sale,
        "all_sales_current_date": all_sales_current_date,
    }
    return render(request, "erp_core/panel_main.html", context)


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    permission_required = "erp_core.view_category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Categories"
        context["url_create"] = reverse_lazy("erp:category-create") 
        return context


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("erp:category-list")
    permission_required = "erp_core.add_category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Category"
        context["url_list"] = reverse_lazy("erp:category-list")
        return context


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("erp:category-list")
    permission_required = "erp_core.change_category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Category"
        context["url_list"] = reverse_lazy("erp:category-list")
        return context


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("erp:category-list")
    permission_required = "erp_core.delete_category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Category"
        context["url_list"] = reverse_lazy("erp:category-list")

        return context


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    permission_required = "erp_core.view_product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Products"
        context["url_create"] = reverse_lazy("erp:product-create")
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("erp:product-list")
    permission_required = "erp_core.add_product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Product"
        context["url_list"] = reverse_lazy("erp:product-list")
        return context


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("erp:product-list")
    permission_required = "erp_core.change_product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Product"
        context["url_list"] = reverse_lazy("erp:product-list")
        return context


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("erp:product-list")
    permission_required = "erp_core.delete_product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Product"
        context["url_list"] = reverse_lazy("erp:product-list")
        return context


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    permission_required = "erp_core.view_client"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Clients"
        context["url_create"] = reverse_lazy("erp:client-create")
        return context


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("erp:client-list")
    permission_required = "erp_core.add_client"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Client"
        context["url_list"] = reverse_lazy("erp:client-list")
        return context


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("erp:client-list")
    permission_required = "erp_core.change_client"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Client"
        context["url_list"] = reverse_lazy("erp:client-list")
        return context


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("erp:client-list")
    permission_required = "erp_core.delete_client"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Client"
        context["url_list"] = reverse_lazy("erp:client-list")
        return context


@login_required
@permission_required("erp_core.view_client", raise_exception=True)
def client_detail_view(request, pk):
    client_data = Client.objects.get(id=pk)
    title = "Client"

    context = {
        "client_data": client_data,
        "title": title,
    }
    return render(request, "erp_core/client_detail.html", context)


@login_required
@permission_required("erp_core.add_sale", raise_exception=True)
def SaleCreateView(request):
    form = SaleForm()
    formset = SaleDetailFormSet()

    if request.method == "POST":
        form = SaleForm(request.POST)
        formset = SaleDetailFormSet(request.POST)

        if form.is_valid():
            SALE = Sale.objects.create(
                client = form.cleaned_data.get("client"),
                comment = form.cleaned_data.get("comment"),
            )

        if formset.is_valid():
            total = 0
            for form in formset:
                product = form.cleaned_data.get("product")
                amount = form.cleaned_data.get("amount")
                try: 
                    product.stock = product.stock - amount
                    product.save()

                except Exception as e:
                    error_message = "Error, Possible cause: "
                    error_message += "The product stock was already at 0 or an attempt was made to add more products than were in the available stock."
                    error_message += f"Error: {e}"
                    print(error_message)
                    return redirect("erp:sale-create")

                if product and amount:
                    sum = float(product.pvp) * float(amount)
                    total += sum
                    SaleDetail(
                        sale=SALE, product=product, amount=amount
                    ).save()

            SALE.total = total
            SALE.save()
        return redirect("erp:sale-list")

    context = {
        "form": form,
        "formset": formset,
    }
    return render(request, "erp_core/sale_form.html", context)


class SaleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Sale
    permission_required = "erp_core.view_sale"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sales"
        context["url_create"] = reverse_lazy("erp:sale-create")
        return context

@login_required
@permission_required("erp_core.view_sale", raise_exception=True)
def sale_detail_view(request, pk):
    sale_specific = Sale.objects.get(id=pk)
    sale_detail_specific = SaleDetail.objects.filter(sale=sale_specific)

    context = {
        "sale_specific": sale_specific,
        "sale_detail_specific": sale_detail_specific,
    }
    return render(request, "erp_core/sale_detail.html", context)


@login_required
@permission_required("erp_core.delete_sale", raise_exception=True)
def sale_delete_view(request, pk):
    sale_specific = Sale.objects.get(id=pk)
    sale_detail_specific = SaleDetail.objects.filter(sale=sale_specific)

    if request.method == "POST":
        sale_specific.delete()
        sale_detail_specific.delete()
        return redirect("erp:sale-list")

    return render(request, "erp_core/sale_confirm_delete.html")
