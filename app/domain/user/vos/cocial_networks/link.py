from typing import Self


class SocialNetworkLink:
    def __init__(
        self: Self,
        value: str,
    ) -> None:
        self.value = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Social network link cannot be empty")

        if not isinstance(self.value, str):
            raise TypeError("Social network link must be a string")

        if not self.value.startswith("https://"):
            raise ValueError("Invalid social network link")
