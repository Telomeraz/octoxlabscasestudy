import base64
import binascii

from rest_framework import authentication, exceptions
from rest_framework.request import Request

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _


class OctoAuthentication(authentication.BaseAuthentication):
    """
    HTTP Octoxlabs authentication against username/password.
    """

    www_authenticate_realm = "api"

    def authenticate(self, request: Request) -> tuple | None:
        """
        Returns a `User` if a correct username and password have been supplied
        using HTTP Octoxlabs authentication.  Otherwise returns `None`.
        """
        auth = authentication.get_authorization_header(request).split()

        if not auth or auth[0].lower() != b"octoxlabs":
            return None

        if len(auth) == 1:
            msg = _("Invalid basic header. No credentials provided.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _("Invalid basic header. Credentials string should not contain spaces.")
            raise exceptions.AuthenticationFailed(msg)

        try:
            try:
                auth_decoded = base64.b64decode(auth[1]).decode("utf-8")
            except UnicodeDecodeError:
                auth_decoded = base64.b64decode(auth[1]).decode("latin-1")
            auth_parts = auth_decoded.partition(":")
        except (TypeError, UnicodeDecodeError, binascii.Error):
            msg = _("Invalid basic header. Credentials not correctly base64 encoded.")
            raise exceptions.AuthenticationFailed(msg)

        userid, password = auth_parts[0], auth_parts[2]
        return self.authenticate_credentials(userid, password, request)

    def authenticate_credentials(self, userid: str, password: str, request: Request = None) -> tuple | None:
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """
        credentials = {get_user_model().USERNAME_FIELD: userid, "password": password}
        user = authenticate(request=request, **credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(_("Invalid username/password."))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_("User inactive or deleted."))

        return (user, None)

    def authenticate_header(self, request: Request) -> str:
        return 'Basic realm="%s"' % self.www_authenticate_realm
