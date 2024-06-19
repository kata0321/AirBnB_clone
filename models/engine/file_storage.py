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
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)
   def reload(self):
       if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
