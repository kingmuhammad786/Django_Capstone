"""
URL configuration for portfolio_project.

Defines all routes, including:
- Admin panel
- Portfolio app views
- Authentication routes
- Serving media files in development
"""
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # ✅ Required for serving media files

urlpatterns = [
    path("accounts/login/", RedirectView.as_view(url="/login/")),
    path('admin/', admin.site.urls),  # ✅ Enables Django admin panel
    path('', include('portfolio.urls')),  # ✅ Main portfolio app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ Authentication URLs
]

# ✅ Enables Django to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

