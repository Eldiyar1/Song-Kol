from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="SonKoulTravel API",
      default_version='v1',
      description="Description of SonKoulTravel API",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="myworkingartur@gmail.com"),
      license=openapi.License(name="POfse License"),
   ),
   public=True,
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]