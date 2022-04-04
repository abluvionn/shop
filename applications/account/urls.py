from django.urls import path, include

from applications.account.views import RegisterApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view())
]