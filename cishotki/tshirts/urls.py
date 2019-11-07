from django.urls import path
from .views import TShirtsView


urlpatterns = [
	path("", TShirtsView.as_view(),  name="tshirts"),
]