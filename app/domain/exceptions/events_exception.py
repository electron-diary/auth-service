from app.domain.base.base_exception import BaseDomainError


class EventValidationError(BaseDomainError):
    ...

class EventsNotFoundError(BaseDomainError):
    ...
