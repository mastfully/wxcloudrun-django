from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TenatView(APIView):

    def post(self, request):
        user = request.user
        data = request.data