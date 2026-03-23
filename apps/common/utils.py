from contextlib import contextmanager

from django.conf import settings
from django.core.mail import send_mail
from django.db import DatabaseError, IntegrityError
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


def send_app_email(subject, message, recipient_list):
    return send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
        fail_silently=True,
    )
