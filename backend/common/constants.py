import enum

__all__ = ["StatusType"]


@enum.unique
class StatusType(enum.Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
