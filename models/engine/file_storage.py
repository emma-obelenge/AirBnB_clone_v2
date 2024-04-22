import json
from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
            self.save()

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        if cls is not None:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        serialized_objs = {key: val.to_dict() for key,
                           val in self.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                self.__objects = {}
                for key, val in data.items():
                    cls_name = val['__class__']
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass
