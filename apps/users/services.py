from django.db import IntegrityError, transaction

from apps.common.exceptions import UserAlreadyExistsException
from apps.common.utils import send_app_email
from apps.users.models import User


class UserService:
    @staticmethod
    @transaction.atomic
    def register_user(email, password, **extra_fields) -> User:
        try:
            user = User.objects.create_user(
                email=email,
                password=password,
                **extra_fields
            )

            send_app_email(
                subject="Welcome to Event Management!",
                message=f"Hello! "
                        f"Your account {user.email} has been successfully created.",
                recipient_list=[user.email]
            )
            return user

        except IntegrityError:
            raise UserAlreadyExistsException()
