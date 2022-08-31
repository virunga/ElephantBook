"""ElephantBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import include, path

admin.site.login = staff_member_required(admin.site.login, login_url="index")

urlpatterns = (
    [
        path("", include("eb_core.urls")),
        path("anno/", include("eb_anno.urls")),
        path("fg/", include("eb_fg.urls")),
        path("api/", include("eb_api.urls")),
        path("rcos_match/", include("rcos_match.urls")),
        path("admin/", admin.site.urls),
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
        path("fp/", include("django_drf_filepond.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]
