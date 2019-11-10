from django.db import models
from users.models import User
from django.utils.translation import ugettext as _
from cishotki.settings import SEX

class Topic(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic

class Tag(models.Model):
    tag = models.CharField(max_length=70)

    def __str__(self):
        return self.tag


class TShirt(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=500, default="")
    topic = models.ManyToManyField(Topic)
    tag = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='uploads/designs')
    sex = models.CharField(max_length=1, choices=SEX)
    uploaded_image = models.ImageField(upload_to='uploads/images')
    background = models.CharField(max_length=15, default="000000")
    is_pattern = models.BooleanField(default=False)


class Rate(models.Model):
    RATES = (
        ('1', "1"),
        ('2', "2"),
        ('3', "3"),
        ('4', "4"),
        ('5', "5"),   
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    tshirt = models.ForeignKey(TShirt,on_delete=models.CASCADE)
    rate = models.CharField(max_length=1, choices=RATES)
