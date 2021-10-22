from django.urls import path, re_path
from django.urls.conf import include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from crud.api.viewsets.UserViewSet import UserViewSet
from crud.api.viewsets.CurrencyViewSet import CurrencyViewSet
from crud.api.viewsets.SafeCurrencyViewSet import SafeCurrencyViewSet
from crud.api.viewsets.TransactionViewSet import TransactionViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="app Api",
        default_version='v1',
        description="app's endpoints",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

route = routers.DefaultRouter()

route.register(r'user', UserViewSet, basename="Users")
route.register(r'currency', CurrencyViewSet, basename="Currencys")
route.register(r'safecurrency', SafeCurrencyViewSet, basename="SafeCurrencys")
route.register(r'transaction', TransactionViewSet, basename="Transactions")

urlpatterns = [
  path('api/v1/', include([
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
          name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
          name='schema-redoc'),
    path('​api-token-auth​/', obtain_jwt_token),
    path('', include(route.urls))
  ]))
]
