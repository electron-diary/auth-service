from dataclasses import dataclass


@dataclass(frozen=True)
class OpenTelemetryConfig:
    endpoint: str
    service_name: str
    environment: str
    version: str
    sample_rate: float
    max_queue_size: int
    export_timeout: int
    max_export_batch_size: int