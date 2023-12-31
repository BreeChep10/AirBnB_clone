#!/usr/bin/python3
"""
a base class
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    a base class for the AirBnB for Dolls
    anything for dolls
    """
    def __init__(self, *args, **kwargs):
        """
        innitializes an instance variables

        Args:
            id - the id of the created instance
            created_at - the time at which  the object was created
            updated_at - the time at which the object was updated
            args - non keyworded argument
            kwargs - keyworded argument(dictionary)
        """
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        returns a string representation of the class
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates the updated_at public instance variable to the current
        time
        """
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict
        """
        store = self.__dict__.copy()

        store.update({"__class__": self.__class__.__name__,
                      "created_at": self.created_at.isoformat(),
                      "updated_at": self.updated_at.isoformat()
                      })
        return store
