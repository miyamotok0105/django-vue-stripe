#これがエラーになるので消した
# from mapper.object_mapper import ObjectMapper

from backend.app.catalog.domain.entities.image import Image
from backend.app.catalog.models import ImageModel


class ImageRepository(object):

    def __init__(self):
        pass

    def all(self):
        images = []
        imageModel = ImageModel.objects.all()
        for image in imageModel.values():
            image = Image(
                    image['image_id'],
                    image['file_path']
                )
            images.append(image.to_dict())
        # print(ItemModel.objects.values_list())
        return images

    def upload(self, image):
        pass

