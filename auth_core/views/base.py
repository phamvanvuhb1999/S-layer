from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed


class AuthenticatedView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)


class BlockDefaultView(AuthenticatedView):

    def get(self, request, *args, **kwargs):
        raise MethodNotAllowed(method=self.request.method)

    def post(self, request, *args, **kwargs):
        raise MethodNotAllowed(method=self.request.method)

    def patch(self, request, *args, **kwargs):
        raise MethodNotAllowed(method=self.request.method)

    def put(self, request, *args, **kwargs):
        raise MethodNotAllowed(method=self.request.method)

    def delete(self, request, *args, **kwargs):
        raise MethodNotAllowed(method=self.request.method)

