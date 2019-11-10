from django.urls import path
from .views import TShirtsView, ForeignTShirtsView, AjaxCommentLoadView, ajax_save_comment
from cishotki.settings import THEME


urlpatterns = [
	path("<int:tshirt_id>/", TShirtsView.as_view(),  name="design_view"),
	path("<str:user_name>/", ForeignTShirtsView.as_view(),  name="foreign_tshirts_view"),
	path("<int:tshirt_id>/comments", AjaxCommentLoadView.as_view(),  name="comments"),
	path("<int:tshirt_id>/comments/add", ajax_save_comment,  name="save_comments"),

]