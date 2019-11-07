from django.db import models
from django.contrib.auth.models import AbstractUser


from cishotki.settings import SEX


class User(AbstractUser):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	sex = models.CharField(max_length=1, choices=SEX)


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	comment = models.TextField(max_length=200)

	def __str__(self):
		return self.comment


class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
