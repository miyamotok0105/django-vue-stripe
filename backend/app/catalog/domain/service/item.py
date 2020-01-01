from backend.app.catalog.domain.repositories.item_repository import ItemRepository

class ItemService(object):
    def __init__(self):
        self.item_repository = ItemRepository()

    def all(self):
        item = self.item_repository.all()
        # return item.all()
        return item