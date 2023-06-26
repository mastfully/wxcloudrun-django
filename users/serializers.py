from rest_framework.serializers import ModelSerializer

from .models import Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsersSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class JfwTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(JfwTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = 'wx_{0}'.format(user.username)
        return token
