from django.forms import (
        ModelForm, 
        TextInput,
        Textarea,
        NumberInput, 
        formset_factory
        )

from .models import (
        Category,
        Product,
        Client, 
        Sale,
        SaleDetail
        )

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
                "name": TextInput(
                    attrs={
                        "placeholder":"Enter Name",
                        "autofocus":"autofocus",
                        }
                    ),
                "description": Textarea(
                    attrs={
                        "placeholder":"Enter Description",
                        }
                    )
                }

class ProductForm(ModelForm):
    class Meta:
        model = Product 
        fields = "__all__"
        widgets = {
                "name":TextInput(
                    attrs={
                        "placeholder":"Enter Name",
                        }
                    ),
                "pvp":NumberInput(
                    attrs={
                        "min":"0",
                        }
                    ),
                }

class ClientForm(ModelForm):
    class Meta:
        model = Client 
        fields = "__all__"
        widgets = {
                "identity_card_number":TextInput(
                    attrs={
                        "placeholder":"Enter Identity Card Number",
                        }
                    ),
                "first_name":TextInput(
                    attrs={
                        "placeholder":"Enter Name",
                        }
                    ),
                "last_name":TextInput(
                    attrs={
                        "placeholder":"Enter LastName",
                        }
                    ),
                "phone_number":TextInput(
                    attrs={
                        "placeholder":"Enter Phone Number",
                        }
                    ),
                "address": Textarea(
                    attrs={
                        "placeholder":"Enter Address",
                        "rows":"3"
                        }
                    ),
                "extra_information": Textarea(
                    attrs={
                        "placeholder":"Enter Extra Information",
                        "rows":"3"
                        }
                    )
                }

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['client','comment',]
        widgets = {
                "comment": Textarea(
                    attrs={
                        "placeholder":"Enter Comment (Optional)",
                        }
                    )
                }


class SaleDetailForm(ModelForm):
    class Meta:
        model = SaleDetail
        fields = ['product','amount',]

SaleDetailFormSet = formset_factory(SaleDetailForm, extra=1)
