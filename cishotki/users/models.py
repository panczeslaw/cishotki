from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _

from .helpers import in_48_hours, generate_confirmation_hash

from cishotki.settings import SEX



class User(AbstractUser):
	#sex = models.CharField(max_length=1, choices=SEX, verbose_name=_("Пол"))
	is_banned = models.BooleanField(default=False, verbose_name=_("Забанен"))
	is_confirmed = models.BooleanField(default=False, verbose_name=_("Confirmed e-mail"))
	confirmation_hash = models.CharField(max_length=100, verbose_name=_("Confirmation hash"), blank=True, null=True)
	#confirmation_expire_datetime = models.DateTimeField(default=in_48_hours)

	def setup_confirmation(self):
		self.is_confirmed = False
		self.confirmation_hash = generate_confirmation_hash(self)
		#self.confirmation_expire_datetime = in_48_hours()
		self.save()




class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	comment = models.TextField(max_length=200)

	def __str__(self):
		return self.comment


class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
