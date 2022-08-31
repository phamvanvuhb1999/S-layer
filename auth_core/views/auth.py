from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import logout
from django.contrib.auth.models import update_last_login

from django.utils.translation import gettext_lazy as _

from auth_core.views import BlockDefaultView
from auth_core.serializers import UserSerializer


class Logout(BlockDefaultView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # Remove token
        request.user.auth_token.delete()
        # clear session
        logout(request)
        return Response(status=status.HTTP_200_OK, data={'message': _('Logout success!')})


class CustomLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        if username is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'username': 'Required username!'})

        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        Token.objects.filter(user=user).delete()
        new_token = Token.objects.create(user_id=user.id)
        update_last_login(sender=__name__, user=user)

        context = {
            **UserSerializer(user).data,
            'token': new_token.key,
        }

        return Response(context)


class CustomSignUp(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

