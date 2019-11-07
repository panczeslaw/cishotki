from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
	fieldsets = UserAdmin.fieldsets + (
		(_("Confirmation info"), {"fields": ("is_confirmed", "confirmation_hash",)},),
	)

	