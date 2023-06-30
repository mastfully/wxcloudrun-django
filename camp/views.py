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
        try:
            JCampTbName.objects.filter(current=True).update(current=False)
            CCampTbName.objects.filter(current=True).update(current=False)
        except:
            pass
        jcamp_data = {
            "tb_name":product_table_name('jcamp',data['year'], data['vacation']),
            "c_name":data['year']+data['vacation']+'精致营',
        }
        ccamp_data = {
            "tb_name": product_table_name('ccamp', data['year'], data['vacation']),
            "c_name": data['year'] + data['vacation'] + '畅享营',
        }
        JCampTbName.objects.update_or_create(**jcamp_data, defaults={'current':True})
        CCampTbName.objects.update_or_create(**ccamp_data, defaults={'current':True})
        Title.objects.all().delete()
        Title.objects.create(**data)
        create_db_table(product_table_name('ccamp', data['year'], data['vacation']))
        create_db_table(product_table_name('jcamp', data['year'], data['vacation']))

        return Response(status=status.HTTP_200_OK)


class SignUpView(APIView):
    def post(self,request):
        data = request.data
        user = request.user
        ser = SignUpSerializer(data=data['camp'])
        if ser.is_valid():
            if data['camp_type'] == 'jcamp':
                try:
                    tb_name = JCampTbName.objects.get(current=True).tb_name
                    jcamp = create_or_get_sign_up_list_model(tb_name)
                    jcamp.objects.create(user=user, **data['camp'])
                    return Response(status=status.HTTP_200_OK)
                except Exception as e:
                    return Response(data={'msg':'服务器出错'},status=status.HTTP_400_BAD_REQUEST)
            if data['camp_type'] == 'ccamp':
                try:
                    tb_name = CCampTbName.objects.get(current=True).tb_name
                    ccamp = create_or_get_sign_up_list_model(tb_name)
                    ccamp.objects.create(user=user, **data['camp'])
                    return Response(status=status.HTTP_200_OK)
                except Exception as e:
                    return Response(data={'msg': '服务器出错'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'msg':'数据不合规'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        pass
