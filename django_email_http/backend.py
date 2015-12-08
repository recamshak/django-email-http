"""HTTP email forwarding backend class."""
import requests

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils import six
from django.core.mail.backends.base import BaseEmailBackend

class HttpEmailBackend(BaseEmailBackend):
    def __init__(self, url=None, *args, **kwargs):
        self.url = url or settings.HTTP_EMAIL_FORWARD_URL
        if not isinstance(self.url, six.string_types):
            raise ImproperlyConfigured('URL for forwarding emails is invalid: %r' % self.url)

        super(HttpEmailBackend, self).__init__(*args, **kwargs)

    def send_messages(self, email_messages):
        if not email_messages:
            return

        try:
            data = [message.__dict__ for message in email_messages]
            requests.post(self.url, data=data)
        except Exception:
            if not self.fail_silently:
                raise
        return len(email_messages)
