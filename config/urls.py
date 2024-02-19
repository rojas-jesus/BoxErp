from django.contrib import admin
from django.urls import include, path
from homepage.views import Index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/', include('erp_core.urls')),
    path('', Index.as_view(), name="index"),
    path('login/',include('login.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
