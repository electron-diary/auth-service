from app.domain.common.common_exceptions import CommonDomainError


class EventValidationError(CommonDomainError):
    ...

class EventsNotFoundError(CommonDomainError):
    ...