from enum import Enum
from django.db import models

def dont_call(cls):
    cls.do_not_call_in_templates = True
    return cls

@dont_call
class ChoiceEnum(Enum):
    
    @classmethod
    def choices(cls):
        res = []

        for name, value in cls._member_map_.items():
            name = name.capitalize().replace("_", " ")
            res += [(name, value.value)]

        return tuple(res)


    def __call__(self):
        return self.value

    @classmethod
    def all(cls):
        return (x for x in cls._member_map_.values())

def add_enum_field(enum, func):
    def modify(cls):
        for name, member in enum._member_map_.items():
            name = name.lower()
            setattr(cls, name, func(member))

        return cls
    return modify

def make_model(cls):
    data = dict(cls.__dict__)
    del data["__dict__"]
    del data["__weakref__"]

    return type(cls.__name__, (models.Model, ), data)

