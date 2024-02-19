from django.urls import path
from .views import LogInView,LogoutView

urlpatterns = [
    path('', LogInView.as_view(),name="log-in"),
    path('logout', LogoutView.as_view(),name="log-out"),
]

