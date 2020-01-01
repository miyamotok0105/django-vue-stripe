
#今は無口なエンティティ
class Item(object):

    def __init__(self, item_id, title, author, read, price):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.read = read
        self.price = price

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'title': self.title,
            'author': self.author,
            'read': self.read,
            'price': self.price
        }
