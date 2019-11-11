from django.db import models

from django.utils import timezone

from tshirts.models import TShirt

class Order(models.Model):
	full_name = models.CharField(max_length=100, verbose_name="Имя и фамилия")
	phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
	email = models.EmailField(verbose_name="Электронная почта")
	cost = models.PositiveIntegerField(verbose_name="Стоимость", default=20)
	tshirt = models.ForeignKey(TShirt, on_delete=models.CASCADE, verbose_name="Майка")
	count = models.PositiveIntegerField(verbose_name="Количество маек")
	address = models.TextField(null=True, blank=True, max_length=500, verbose_name="Адрес")
	seed = models.CharField(max_length=30, verbose_name="Сид")
	sign = models.CharField(max_length=100, verbose_name="Подпись")
	webpay_transaction_id = models.CharField(null=True, blank=True, max_length=100, verbose_name="ID транзакции в Webpay", help_text="Указан, если оплачено онлайн")
	delivered = models.BooleanField(default=False, verbose_name="Явка")
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "{} ({} {})".format(self.tshirt, self.full_name, self.phone_number)