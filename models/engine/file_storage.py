import json
import os

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
   def save(self):
        with open(self.__file_path, 'w') as f:
            json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(json_objects, f)
   def reload(self):
       if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                 for obj_dict in json_objects.values():
                    cls_name = obj_dict['__class__']
                    cls = globals()[cls_name]
                    self.new(cls(**obj_dict))
