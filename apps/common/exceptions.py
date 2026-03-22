from rest_framework.views import exception_handler
from rest_framework.exceptions import (
    APIException,
    ValidationError,
    AuthenticationFailed,
    PermissionDenied
)
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        code = getattr(exc, "default_code", "error")

        if isinstance(exc, ValidationError):
            code = "validation_error"
        elif isinstance(exc, AuthenticationFailed):
            code = "unauthorized"
        elif isinstance(exc, PermissionDenied):
            code = "access_denied"

        message = "An error occurred"

        if isinstance(response.data, dict):
            if "detail" in response.data:
                message = response.data["detail"]
            elif response.data:
                first_key = next(iter(response.data))
                first_val = response.data[first_key]

                error_text = first_val[0] if isinstance(first_val, list) and first_val else first_val

                message = f"{first_key}: {error_text}" if first_key != "non_field_errors" else error_text

        elif isinstance(response.data, list) and response.data:
            message = response.data[0]

        response.data = {
            "status": "error",
            "code": code,
            "message": str(message),
            "details": response.data
        }

    return response


class BaseAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "An error occurred while processing the request."
    default_code = "error"


class UserAlreadyExistsException(BaseAPIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "A user with this email already exists."
    default_code = "user_exists"


class EventFullException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "There are no more seats available for this event."
    default_code = "event_full"


class UnauthorizedException(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Authentication credentials were not provided or are invalid."
    default_code = "unauthorized"


class AccessDeniedException(BaseAPIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You do not have permission to perform this action."
    default_code = "access_denied"
