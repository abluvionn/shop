
from django.conf.urls.static import static
from django.urls import include

from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from shop import settings

schema_view = get_schema_view(openapi.Info(title = 'Python18 Shop Project',
                                           description = 'internet shop',
                                           default_version='v1',),
                              public=True
                              )




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', include('applications.product.urls')),
    path('api/v1/account/', include('applications.account.urls')),
    path('swagger/',schema_view.with_ui('swagger')),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

