from models import storage
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key_value in kwargs.items():

                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        elf.updated_at = datetime.now()
        storage.save()
    def to_dict(self):
        dict_provide = self.__dict__.copy()
        dict_provide['__class__'] = self.__class__.__name__
        dict_provide['created_at'] = self.created_at.isoformat()
        dict_provide['updated_at'] = self.updated_at.isoformat()
        return dict_provide
