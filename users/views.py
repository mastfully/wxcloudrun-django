from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_204_NO_CONTENT
import logging
from weixin import WXAPPAPI
from weixin.oauth2 import OAuth2AuthExchangeError
from wxcloudrun import settings
from .utils import GetOpenId


# Create your views here.
from .models import *
from .serializers import *

logger = logging.getLogger('django')


def create_or_update_user_info(openid, ):
    """
    创建或者更新用户信息
    :param openid: 微信 openid
    :param tenat_id: 微信用户信息
    :return: 返回用户对象
    """
    if openid:
        user, created = Users.objects.update_or_create(openid=openid, )
        return user
    return None


class LoginView(APIView):
    """
        post:
        微信登录接口
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        code = request.data.get('code')
        if code:
            session_info = GetOpenId(appid=settings.APPID,appsecret=settings.APPSECRET)
            try:
                session_info = session_info.get_session(code=code)
            except OAuth2AuthExchangeError:
                session_info = None
            if session_info:
                openid = session_info.get('openid')
                user = create_or_update_user_info(openid,)
                if user:
                    token = JfwTokenObtainPairSerializer.get_token(user).access_token
                    return Response(
                        {
                            'token': str(token),
                            'openid': openid,
                        },
                        status=HTTP_200_OK)
        return Response({'token': None, 'user': {}}, status=HTTP_204_NO_CONTENT)
