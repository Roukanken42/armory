from enum import Enum

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
