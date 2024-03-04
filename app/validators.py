import re

from wtforms.validators import Regexp


class PasswordRestrictions:
    def __init__(self):
        self.message = ''
        self._validators = [
            Regexp(regex='.*[0-9].*', message='Password must contain digit'),
            Regexp(regex='.*[a-zA-Z].*', message='Password must contain letter')
        ]

    def __call__(self, form, field, message=None):
        for validator in self._validators:
            validator(form, field)

        return True
