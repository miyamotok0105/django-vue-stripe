from backend.app.catalog.domain.repositories.image_repository import ImageRepository


class ImageService(object):
    def __init__(self):
        self.image_repository = ImageRepository()

    def get_all(self):
        image = self.image_repository.all()
        return image

    def upload(self, id, image):
        pass
        # charge = self.image_repository.upload()
        # return charge
