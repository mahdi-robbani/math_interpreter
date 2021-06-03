from enum import Enum
from dataclasses import dataclass

###############################
#Convert input string to tokens
###############################

# Assign a number to each type of token
class TokenType(Enum):
    """Maps each constant token name to a number"""

    NUMBER      = 0
    PLUS        = 1
    MINUS       = 2
    MULTIPLY    = 3
    DIVIDE      = 4
    LPAREN      = 5
    RPAREN      = 6

@dataclass
class Token:
    """Class for all token types. A token is grouping of the input string. Each 
    token has a type and optionally a value. e.g. a NUMBER token and with a 
    of 3. The @dataclass decorater adds some automatic funcionality such as
    __init__ and __repr__ etc.
    """

    type: TokenType # we are initilizing using fields, part of @dataclass
    value: any = None 

    def __repr__(self) -> str:
        # Print name+value if value exists
        return self.type.name + (f":{self.value}" if self.value is not None else "")

