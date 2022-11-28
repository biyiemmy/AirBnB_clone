#!/usr/bin/python3
"""This script is the base model"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    ''''Class from which all other classes will inherit'''
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''Returns official string representation'''
        return (f"[{self.__class__.__name__}] ({self.id}) \
{str(self.__dict__)}")

    def save(self):
        '''updates the public instance attribute updated_at'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dic__'''
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic

    def __init__(self, *args, **kwargs):
        '''Initializes instance attributes'''
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key in kwargs.keys():
                # check and escape the __class__ key
                if key == "__class__":
                    continue
                else:
                    # check and change the format for updated_at & created_at
                    if key == "updated_at" or key == "created_at":
                        kwargs[key] = datetime.datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    # set the attributes of the instance
                    setattr(self, key, kwargs[key])
