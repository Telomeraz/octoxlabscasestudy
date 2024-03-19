from django.urls import path

from .views import ConvertQueryView

urlpatterns = [
    path("", ConvertQueryView.as_view(), name="convert_query"),
]
