
#今は無口なエンティティ
class File(object):

    def __init__(self, file, remark, timestamp):
        self.file = file
        self.remark = remark
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'file': self.file,
            'remark': self.remark,
            'timestamp': self.timestamp
        }
