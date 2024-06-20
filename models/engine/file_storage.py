#!/usr/bin/python3
import datatime
import json
import os

class FileStorage:
    _file_path = 'file.json'
    _objects = {}
    def all(self):
        return self._objects
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self._objects[key] = obj
   def save(self):
        with open(self.__file_path, 'w') as f:
            json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, f)
   def reload(self):
       if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                 for obj_dict in json_objects.values():
                    cls_name = obj_dict['__class__']
                    cls = globals()[cls_name]
                    self.new(cls(**obj_dict))
