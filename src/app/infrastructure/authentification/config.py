from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TokensConfig:
    access_token_expires_minutes: int = 15
    refresh_token_expires_days: int = 30
    secret_key: Path
    algorithm: str
    public_key: Path