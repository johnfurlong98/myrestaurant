# accounts/decorators.py

from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def role_required(role):
    """
    Decorator for views that checks whether the user has a specific role.
    """
    def check_role(user):
        if user.is_authenticated and user.role == role:
            return True
        raise PermissionDenied
    return user_passes_test(check_role)
