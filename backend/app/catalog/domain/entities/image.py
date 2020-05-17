
#今は無口なエンティティ
class Image(object):

    def __init__(self, image_id, file_path):
        self.image_id = image_id
        self.file_path = file_path

    def to_dict(self):
        return {
            'image_id': self.image_id,
            'file_path': self.file_path
        }
