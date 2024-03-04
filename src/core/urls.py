from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.drf_yasg import urlpatterns as urls_swagger


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main_page.urls")),
    path("", include("blog_and_news.urls")),
    path("", include("client_actions.urls")),
    path('summernote/', include('django_summernote.urls')),
] + urls_swagger


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]