from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .utils import *
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
        title = Title.objects.all()[0]
        title = TitleSerializer(title).data
        data['jcamps'] = jcamps
        data['ccamps'] = ccamps
        data['title'] = title

        return Response(data=data,status=status.HTTP_200_OK)


class SetTbView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        data = request.data
        jcamp_data = {
            "tb_name":product_table_name('jcamp',data['year'], data['vacation']),
            "c_name":data['year']+data['vacation']+'精致营',
            "current":True
        }
        ccamp_data = {
            "tb_name": product_table_name('ccamp', data['year'], data['vacation']),
            "c_name": data['year'] + data['vacation'] + '畅享营',
            "current": True
        }
        try:
            JCampTbName.objects.create(**jcamp_data)
            CCampTbName.objects.create(**ccamp_data)
        except:
            return Response(data={'msg':'表已经存在'}, status=status.HTTP_201_CREATED)
        Title.objects.all().delete()
        Title.objects.create(**data)
        create_db_table(product_table_name('ccamp', data['year'], data['vacation']))
        create_db_table(product_table_name('jcamp', data['year'], data['vacation']))

        return Response(status=status.HTTP_200_OK)


class SignUpView(APIView):
    def post(self,request):
        data = request.data
        ser = SignUpSerializer(data.camp)
        if ser.is_valid():
            if data.camp_type == 'jcamp':
                tb_name = JCampTbName.objects.get(current=True)
                jcamp = create_or_get_sign_up_list_model(tb_name)
                jcamp.objects.create(**data)
                return Response(status=status.HTTP_200_OK)
            if data.camp_type == 'ccamp':
                tb_name = CCampTbName.objects.get(current=True)
                ccamp = create_or_get_sign_up_list_model(tb_name)
                ccamp.objects.create(**data)
                return Response(status=status.HTTP_200_OK)

    def get(self, request):
        pass
