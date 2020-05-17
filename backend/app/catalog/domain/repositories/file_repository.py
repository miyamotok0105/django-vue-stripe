#これがエラーになるので消した
# from mapper.object_mapper import ObjectMapper

from backend.app.catalog.domain.entities.file import File
from backend.app.catalog.models import FileModel


class FileRepository(object):

    def __init__(self):
        pass

    def all(self):
        files = []
        fileModel = FileModel.objects.all()
        for file in fileModel.values():
            file = File(
                    file['file'],
                    file['remark'],
                    file['timestamp']
                )
            files.append(file.to_dict())
        return files

    # def upload(self, image):
    #     pass

