from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("redirect.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "redirect.views.handler404"
handler500 = "redirect.views.handler500"