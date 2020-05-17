from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=32)
#     mail = models.EmailField()

class ItemModel(models.Model):
    item_id = models.IntegerField()
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    read = models.BooleanField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

class ImageModel(models.Model):
    image_id = models.IntegerField()
    image_file = models.ImageField(upload_to = 'image_file')

class FileModel(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

