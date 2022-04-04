from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from applications.account.serializer import RegisterSerializer
from rest_framework import status
class RegisterApiView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            massage = 'you sucsessfully registrated.We send you activation code to your email'
            return Response(massage,status=201)
        return Response(status=status.HTTP_400_BAD_REQUEST)

