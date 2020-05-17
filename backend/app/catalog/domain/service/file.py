from backend.app.catalog.domain.repositories.file_repository import FileRepository

class FileService(object):
    def __init__(self):
        self.file_repository = FileRepository()

    def get_all(self):
        file = self.file_repository.all()
        return file

    # def upload(self, id, image):
    #     pass
    #     # charge = self.image_repository.upload()
    #     # return charge
