from dataclasses import dataclass

"""This file contains all the output classes of the interpreter. We're
using classes in case we want to extend it in the future."""

@dataclass
class RealNumber:
    value: float

    def __repr__(self) -> str:
        return f"{self.value}"
