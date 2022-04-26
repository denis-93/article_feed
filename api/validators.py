import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class PasswordValidator:

    def validate(self, password, user=None):
        pattern = r'[0-9]'
        if not bool(re.search(pattern, password)):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну цифру!"),
                code='password_doesnt_have_numbers',
            )
