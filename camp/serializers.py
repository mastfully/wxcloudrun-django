from rest_framework.serializers import ModelSerializer

from .models import *


class CCampSerializer(ModelSerializer):

    class Meta:
        model = CCamp
        fields = '__all__'


class JCampSerializer(ModelSerializer):
    class Meta:
        model = JCamp
        fields = '__all__'
