from fastapi import status

from .base import BaseApiException


class UniqueViolation(BaseApiException):
    message = "Not unique"
    status_code = status.HTTP_409_CONFLICT


class EmptyResult(BaseApiException):
    message = "Empty result"
    status_code = status.HTTP_404_NOT_FOUND


class ForeignKeyViolation(BaseApiException):
    message = "Incorrect values"
    status_code = status.HTTP_400_BAD_REQUEST


class CheckViolation(BaseApiException):
    message = "Incorrect values, check violation"
    status_code = status.HTTP_400_BAD_REQUEST


class NumericValueOutOfRange(BaseApiException):
    message = "Incorrect values, too big"
    status_code = status.HTTP_400_BAD_REQUEST


class DriverError(BaseApiException):
    message = "Internal driver error"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
