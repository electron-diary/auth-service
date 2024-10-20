from dataclasses import dataclass

@dataclass(frozen=True)
class UserNameGeneratorConfig:
    prefix: str = 'anonymous-user'
