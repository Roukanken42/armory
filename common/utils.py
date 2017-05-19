from enum import Enum
from django.db import models
from django.core.exceptions import ValidationError

def dont_call(cls):
    cls.do_not_call_in_templates = True
    return cls

@dont_call
class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        res = []

        for name, value in cls._member_map_.items():
            res += [(value.value, value.display_name())]

        return tuple(res)

    def __call__(self):
        return self.value

    def display_name(self):
        return self.name.capitalize().replace("_", " ")

    def __hash__(self):
        return super().__hash__()

    def __eq__(self, other):
        if self.value == other:
            return True

        return super(ChoiceEnum, self).__eq__(other)


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

class EnumField(models.Field):
    def __init__(self, enum, *args, **kwargs):
        self.enum = enum
        kwargs["choices"] = enum.choices()
        super(EnumField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(EnumField, self).deconstruct()
        return name, path, [self.enum] + args, kwargs

    def from_db_value(self, value, expression, connection, context):
        # value = super(EnumField, self).from_db_value(value, expression, connection, context)
        
        if value is None:
            return value

        return self.enum(value)

    def to_python(self, value):
        if isinstance(value, self.enum):
            return value

        if value is None:
            return value

        return self.enum(int(value))


    def get_prep_value(self, value):
        if value is None:
            return None

        value = self.to_python(value).value
        value = super(EnumField, self).get_prep_value(value)
        return value

    def get_internal_type(self):
        return "IntegerField"

