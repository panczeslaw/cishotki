from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _
from .models import User, Comment, Like

@admin.register(User)
class CustomUserAdmin(UserAdmin):
	fieldsets = UserAdmin.fieldsets + (
		(_("Confirmation info"), {"fields": ("is_confirmed", "confirmation_hash",)},),
	)

@admin.register(Comment)	
class CommentAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "comment")
	search_fields = ("user", "comment")
	autocomplete_fields = ("user", )

@admin.register(Like)	
class LikeAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "comment")
	autocomplete_fields = ("user", "comment" )