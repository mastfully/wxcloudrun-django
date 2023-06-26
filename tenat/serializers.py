from rest_framework.serializers import ModelSerializer

from .models import Tenat


class TenatSerializer(ModelSerializer):

    class Meta:
        model = Tenat
        fields = '__all__'
