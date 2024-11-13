from dataclasses import dataclass , field


@dataclass
class BaseSample:
    name:str
    second_name:str =field(default="milind")
    surname:str 


print(BaseSample())