
#今は無口なエンティティ
class Item(object):

    def __init__(self, item_id, title, author, read, price):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.read = read
        self.price = price
        # self._item_id = item_id
        # self._title = title
        # self._author = author
        # self._read = read
        # self._price = price

    # @property
    # def item_id(self):
    #     return self._item_id

    # @property
    # def title(self):
    #     return self._title

    # @property
    # def author(self):
    #     return self._author

    # @property
    # def read(self):
    #     return self._read

    # @property
    # def price(self):
    #     return self._price
