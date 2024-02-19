from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserForm

    fieldsets = (*UserAdmin.fieldsets,
        ('User Iamge and Phone Number', {
            'fields': ('image', 'phone')
        })
    )

admin.site.register(CustomUser,CustomUserAdmin)
