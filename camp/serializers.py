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


class TitleSerializer(ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class JCampTbNameSerializer(ModelSerializer):
    class Meta:
        model = JCampTbName
        fields = '__all__'


class CCampTbNameSerializer(ModelSerializer):
    class Meta:
        model = CCampTbName
        fields = '__all__'


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = BaseSignUpListModel
        fields = '__all__'


class TenatCampPriceSerializer(ModelSerializer):
    class Meta:
        model = TenatCampPrice
        fields = '__all__'
