from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

class LoginAPI(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)

            if serializer.is_valid():
                user_type = serializer.validated_data.get('user_type')
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')

                is_user = False
                data = None
                try:
                    user = User.objects.get(email=email)

                    is_user = authenticate(request=request, username=user.username, password=password)
                except:
                    return Response({'success':False, 'error':'Girilen bilgilerde kullanıcı bulunamadı.'}, status=status.HTTP_400_BAD_REQUEST)

                if is_user:
                    login(request, user)

                    if user_type == 'Regional Director':
                        regional = RegionalDirector.objects.get(user=user)
                        data = regional.user_uuid
                    elif user_type == 'Marketing Manager':
                        marketing = MarketingManager.objects.get(user=user)
                        data = marketing.user_uuid
                    elif user_type == 'District Manager':
                        district = DistrictManager.objects.get(user=user)
                        data = district.user_uuid
                    else:
                        return Response({'success':False, 'error':'Hata!'}, status=status.HTTP_400_BAD_REQUEST)
                

                return Response({'success':True, 'data':data}, status=status.HTTP_200_OK)
            else:
                return Response({'success':False, 'error':'Data is not valid!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'success':False, 'error':'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)