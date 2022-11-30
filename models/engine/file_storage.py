#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            return {k: v for k, v in FileStorage.__objects.items()
                    if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if exists(self.__file_path):
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
            dummy = None
            for key, value in data.items():
                dummy = self.classes[key.split('.')[0]](**value)
                FileStorage.__objects[key] = dummy

    def delete(self, obj=None):
        """ Deletes an object """
        if obj is None:
            return
        else:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.all():
                del self.all()[key]
                self.save()

    def close(self):
        """ Deserializes the JSON file to objects """
        self.reload()

# #!/usr/bin/python3
# """This module defines a class to manage file storage for hbnb clone"""
# import json


# class FileStorage:
#     """This class manages storage of hbnb models in JSON format"""
#     __file_path = 'file.json'
#     __objects = {}

#     def all(self, cls=None):
#         """Returns a dictionary of models currently in storage"""
#         if cls is None:
#             return FileStorage.__objects

#         elif FileStorage.__objects:
#             objs_result = {}
#             # Checks each object inside __objects:
#             for key, value in self.__objects.items():
#                 if cls == type(value):
#                     objs_result[key] = value
#             # In objs_result we save all the filtered results:
#             return objs_result

#     def new(self, obj):
#         """Adds new object to storage dictionary"""
#         self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

#     def save(self):
#         """Saves storage dictionary to file"""
#         with open(FileStorage.__file_path, 'w') as f:
#             temp = {}
#             temp.update(FileStorage.__objects)
#             for key, val in temp.items():
#                 temp[key] = val.to_dict()
#             json.dump(temp, f)

#     def reload(self):
#         """Loads storage dictionary from file"""
#         from models.base_model import BaseModel
#         from models.user import User
#         from models.place import Place
#         from models.state import State
#         from models.city import City
#         from models.amenity import Amenity
#         from models.review import Review

#         classes = {
#                     'BaseModel': BaseModel, 'User': User, 'Place': Place,
#                     'State': State, 'City': City, 'Amenity': Amenity,
#                     'Review': Review
#                   }
#         try:
#             temp = {}
#             with open(FileStorage.__file_path, 'r') as f:
#                 temp = json.load(f)
#                 for key, val in temp.items():
#                     self.all()[key] = classes[val['__class__']](**val)
#         except FileNotFoundError:
#             pass

#     def delete(self, obj=None):
#         """Deletes an object from the storage __objects"""
#         if obj is None:
#             return
#         else:
#             # In JSON file we save all the new objects like:
#             # Place.213bhj231af3 = name of the object "." object.id:
#             key = "{}.{}".format(type(obj).__name__, obj.id)

#             try:
#                 del self.__objects[key]
#                 self.save()
#             # If the key isn't in __objects raises and exception:
#             except Exception:
#                 pass

#     def close(self):
#         """ Close function, deserializes the JSON file to Python objects"""
#         self.reload()
