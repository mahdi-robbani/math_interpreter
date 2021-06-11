#from enum import Enum
from dataclasses import dataclass

@dataclass
class Token:
    """Class for all token types. A token is grouping of the input string. Each 
    token has a type and optionally a value. e.g. a NUMBER token and with a 
    of 3. The @dataclass decorater adds some automatic funcionality such as
    __init__ and __repr__ etc.
    """

    type: str # we are initilizing using fields, part of @dataclass
    value: any = None 

    def __repr__(self) -> str:
        # Print name+value if value exists
        return self.type + (f":{self.value}" if self.value is not None else "")
