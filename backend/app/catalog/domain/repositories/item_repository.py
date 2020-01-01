#これがエラーになるので消した
# from mapper.object_mapper import ObjectMapper

from backend.app.catalog.domain.entities.item import Item
from backend.app.catalog.models import ItemModel


class ItemRepository(object):

    def __init__(self):
        pass

    def all(self):
        items = []
        itemModel = ItemModel.objects.all()
        # print(itemModel.values())
        for item in itemModel.values():
            item = Item(
                    item['item_id'],
                    item['title'],
                    item['author'],
                    item['read'],
                    item['price']
                )
            items.append(item.to_dict())
        # print(ItemModel.objects.values_list())
        return items

    def save(self, item):
        pass
