from django.db import models

# Create your models here.


class Clerk(models.Model):
    id = models.AutoField(primary_key=True)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)