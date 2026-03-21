from contextlib import contextmanager
from django.db import IntegrityError, DatabaseError
from rest_framework.exceptions import ValidationError


@contextmanager
def database_errors_boundary():
    try:
        yield
    except IntegrityError as e:
        raise ValidationError(
            {"detail": f"Database integrity error: {str(e)}"}
        )
    except DatabaseError:
        raise ValidationError(
            {"detail": "A database error occurred."}
        )
