from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'full_name', 'phone_number_link', 'email_link', 'tshirt', 'count', 'address', 'webpay_transaction_id', 'delivered')
	readonly_fields = ('seed', 'sign',)
	date_hierarchy = 'date'

	def phone_number_link(self, obj):
		return format_html('<a href="tel:{0}">{0}</a>'.format(obj.phone_number))
	

	def email_link(self, obj):
		return format_html('<a href="mailto:{0}">{0}</a>'.format(obj.email))
	
