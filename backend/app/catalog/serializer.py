# coding: utf-8

from rest_framework import serializers

from .models import ItemModel


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ('item_id', 'title', 'author', 'read', 'price')

# class ItemSerializer(object):

#     @staticmethod
#     def serialize(item):
#         return {
#             'item_id': item.item_id,
#             'title': item.title,
#             'author': item.author,
#             'read': item.read,
#             'price': item.price
#         }