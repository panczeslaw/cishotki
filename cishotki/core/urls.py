from django.urls import path
from .views import main, about, ConstructorView


urlpatterns = [
	path("", main,  name="main"),
	path("about/", about, name="about"),
	path("constructor/", ConstructorView.as_view(), name="constructor"),
]