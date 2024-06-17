#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """BaseModel defines all common attributes/methods for other classes."""
    def __init__(self):
        """Initialize a new BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    def __str__(self):
         """Return string"""
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"
    def save(self):
        """Update the updated_at"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """Return a dictionary containing all keys/values"""
        dict_provide = self.__dict__copy()
        dict_provide['__class__'] = self.__class__.__name__
        dict_provide['created_at'] = self.created_at.isoformat()
        dict_provide['updated_at'] = self.updated_at.isoformat()
        return dict_provide
