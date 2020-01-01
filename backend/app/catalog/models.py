from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=32)
#     mail = models.EmailField()

class Item(models.Model):
    item_id = models.IntegerField()
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    read = models.BooleanField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


