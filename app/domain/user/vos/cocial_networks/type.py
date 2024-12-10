from typing import Self, Literal


social_network_types = Literal[
    "twitter", "instagram", "tiktok", "vk", "telegram", "youtube", "facebook", "discord"
]


class SocialNetworkType:
    def __init__(
        self: Self,
        value: str
    ) -> None:
        self.value = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Social network type cannot be empty")
        
        if self.value not in social_network_types.__args__:
            raise ValueError(f"Invalid social network type: {self.value}")