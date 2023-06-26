from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
# Create your views here.


class CampsView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = {}
        jcamps = JCamp.objects.all()
        ccamps = CCamp.objects.all()
        jcamps = JCampSerializer(jcamps, many=True).data
        ccamps = CCampSerializer(ccamps, many=True).data
        data['jcamps'] = jcamps
        data['ccamps'] = ccamps

        return Response(data=data,status=status.HTTP_200_OK)