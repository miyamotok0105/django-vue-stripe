from backend.app.catalog.domain.repositories.item_repository import ItemRepository

class ItemService(object):
    def __init__(self):
        self.item_repository = ItemRepository()

    def get_all(self):
        item = self.item_repository.all()
        return item

    def charge(self):
        charge = self.item_repository.charge()
        return charge
