from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from catalog.views import ProductListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
    path("blog/", include("blog.urls", namespace="blog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
