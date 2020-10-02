from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=1000)


class ItemHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    note = models.TextField()

