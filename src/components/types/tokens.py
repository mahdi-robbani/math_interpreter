from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    """Class for the allowed token types"""

    NUMBER      = 0
    PLUS        = 1
    MINUS       = 2
    MULTIPLY    = 3
    DIVIDE      = 4
    LPAREN      = 5
    RPAREN      = 6
    EXPONENT    = 7

@dataclass
class Token:
    """Class for all token types. A token is grouping of the input string. Each 
    token has a type and optionally a value. e.g. a NUMBER token and with a 
    of 3. The @dataclass decorater adds some automatic funcionality such as
    __init__ and __repr__ etc.
    """

    # we are initilizing using fields, part of @dataclass
    type: TokenType # Only allow the enumerated token types
    value: any = None 

    def __repr__(self) -> str:
        # Print name+value if value exists
        return self.type.name + (f":{self.value}" if self.value is not None else "")
