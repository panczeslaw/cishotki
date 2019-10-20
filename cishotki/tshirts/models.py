from django.db import models
from users.models import User
from django.utils.translation import ugettext as _
from cishotki.settings import SEX, SIZES

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
    topics = models.ManyToManyField(Topic)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='uploads/images', blank=True)
    size = models.CharField(max_length=3,choices=SIZES)
    sex = models.CharField(max_length=1,choices=SEX)


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


# Create your models here.
