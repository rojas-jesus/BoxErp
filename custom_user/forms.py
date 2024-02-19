from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = "__all__"

