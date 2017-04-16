from enum import Enum

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

    def __int__(self):
        return self()