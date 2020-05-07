from django.db import models
from django.contrib.auth.models import User


class Requisite(models.Model):
    card_number = models.CharField(max_length=24)
    type = models.CharField(max_length=24,blank=True, null=True, default=None)

    def __str__(self):
        return "%s""%s" % (self.card_number,self.type)

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'


class Dialog(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
        user_meessage = models.TextField(blank=True, null=True, default=None)
        admin_meessage = models.TextField(blank=True, null=True, default=None)
        date = models.DateTimeField(auto_now_add=True, auto_now=False)


