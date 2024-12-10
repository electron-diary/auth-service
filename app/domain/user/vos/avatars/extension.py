from typing import Self, Literal


extensions = Literal["jpg", "png", "gif", "jpeg", "webp"]


class Extension:
    def __init__(
        self: Self,
        value: extensions,
    ) -> None:
        self.value: extensions = value

        self.validate()
    
    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Extension cannot be empty")
        
        if self.value not in ["jpg", "png", "gif", "jpeg", "webp"]:
            raise ValueError("Extension must be a valid image extension")