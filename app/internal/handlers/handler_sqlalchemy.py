import functools

from asyncpg import ForeignKeyViolationError, UniqueViolationError
from sqlalchemy.exc import (
    AmbiguousForeignKeysError,
    DataError,
    IntegrityError,
    NoForeignKeysError,
    NoReferencedColumnError,
    NoReferencedTableError,
    NoReferenceError,
    NoResultFound,
    ProgrammingError,
    SQLAlchemyError,
)

from ..schemes.exceptions import *


def __handle_exception(func):
    """Decorator Catching PostgreSQL Query Exceptions.

    Args:
        func: callable function object

    Returns:
        Result of call function.
    Raises:
        UniqueViolation: The query violates the domain uniqueness constraints
            of the database set
        DriverError: Invalid database query
        CheckViolation: Input or calculated values violate check constraint
    """

    async def wrapper(*args: object, **kwargs: object):
        try:
            return await func(*args, **kwargs)
        except NoResultFound:
            raise EmptyResult
        except (
            AmbiguousForeignKeysError,
            NoForeignKeysError,
            NoReferenceError,
            NoReferencedColumnError,
            NoReferencedTableError,
        ) as e:
            print(e)
            raise ForeignKeyViolation
        except IntegrityError as e:
            print(e)
            if isinstance(e.orig.__cause__, ForeignKeyViolationError):
                raise ForeignKeyViolation
            elif isinstance(e.orig.__cause__, UniqueViolationError):
                raise UniqueViolation
            raise CheckViolation
        except DataError as e:
            print(e)
            raise NumericValueOutOfRange
        except ProgrammingError as e:
            print(e)
        except ValueError as e:
            print(e)
        except SQLAlchemyError as e:
            print(e)
            raise DriverError(message=e.code)

    return wrapper


def collect_response(fn=None):
    @functools.wraps(fn)
    @__handle_exception
    async def inner(*args: object, **kwargs: object):
        response = await fn(*args, **kwargs)

        if response is None:
            if "return" in fn.__annotations__:
                return_class = fn.__annotations__["return"]
                if return_class is None:
                    return response
                if hasattr(return_class, "__origin__"):
                    return_class = return_class.__origin__
                if isinstance([], return_class):
                    return []
            raise EmptyResult

        return response

    return inner
