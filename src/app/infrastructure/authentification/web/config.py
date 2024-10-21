from dataclasses import dataclass
from pathlib import Path
from datetime import timedelta

@dataclass(frozen=True)
class AuthConfig:
    secret_key: Path
    public_key: Path
    algorithm: str
    access_expire_minutes: timedelta
    refresh_expire_days: timedelta


