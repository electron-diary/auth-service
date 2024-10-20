from dataclasses import dataclass
from pathlib import Path
from datetime import timedelta

@dataclass(frozen=True)
class AuthConfig:
    secret_key: Path
    public_key: Path
    algorithm: str
    secret_key_expire_minutes: timedelta
    public_key_expire_days: timedelta


