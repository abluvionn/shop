from django.urls import path

from applications.product.views import ListCreateView

urlpatterns = [
    path('', ListCreateView.as_view())
    path('<int:pk>/',DeleteUpdateRetrivieve)
]