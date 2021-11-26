from django.shortcuts import render

# if###########################################
from http import HTTPStatus
from django.http import HttpResponse
############################################


from rest_framework import serializers

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializer

# from .serializer import UserSerializer
from user_api.serializer import UserSerializer
# DefaultSerializer 추가함
from user_api.serializer import DefaultSubSerializer
from user_api.serializer import SubSerializer

from .models import DefaultSubscription, Subscription, User

#if###########################################
class HttpResponseNoContent(HttpResponse):
    status_code = HTTPStatus.NO_CONTENT
###########################################

class DefaultSubView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('service_name') is None:
            default_queryset = DefaultSubscription.objects.all()
            default_queryset_serialier = DefaultSubSerializer(default_queryset, many=True)
            return Response(default_queryset_serialier.data, status=status.HTTP_200_OK)
        else:
            default_id = kwargs.get('service_name')
            default_serializer = DefaultSubSerializer(DefaultSubscription.objects.get(id=default_id)) #id에 해당하는 User의 정보를 불러온다
            return Response(default_serializer.data, status=status.HTTP_200_OK)
            
class SubView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('plan_name') is None:
            sub_queryset = Subscription.objects.all()
            sub_queryset_serialier = SubSerializer(sub_queryset, many=True)
            return Response(sub_queryset_serialier.data, status=status.HTTP_200_OK)
        else:
            sub_id = kwargs.get('plan_name')
            sub_serializer = SubSerializer(Subscription.objects.get(id=sub_id)) #id에 해당하는 User의 정보를 불러온다
            return Response(sub_serializer.data, status=status.HTTP_200_OK)
            

class UserView(APIView):
    # def get(self, request, **kwargs):
    #     # return Response("get ok", status=status.HTTP_200_OK)
    #     if kwargs.get('uid') is None:
    #         users = User.objects.all()
    #         serializer = UserSerializer(users, many=True)
    #     # 이렇게만 해도 되지만 
    #     # return Response(serializer.data, status = status.HTTP_200_OK)

    #     # mata data를 넣어주기 위해
    #         return Response({'count': users.count(), 'data': serializer.data}, status = status.HTTP_200_OK)
    #     else:
    #         uid = kwargs.get('uid')
    #         user = User.objects.get(id=uid)
    #         serializer = UserSerializer(user)
    #         return Response(user, status = status.HTTP_200_OK)
    def get(self, request,  **kwargs):
        if kwargs.get('user_id') is None:
            user_queryset = User.objects.all() #모든 User의 정보를 불러온다.
            user_queryset_serializer = UserSerializer(user_queryset, many=True)
            # return Response(user_queryset_serializer.data, status=status.HTTP_200_OK)
            return Response({'count': user_queryset.count(), 'data': user_queryset_serializer.data}, status = status.HTTP_200_OK)
        else:
            user_id = kwargs.get('user_id')
            user_serializer = UserSerializer(User.objects.get(id=user_id)) #id에 해당하는 User의 정보를 불러온다
            return Response(user_serializer.data, status=status.HTTP_200_OK)
#####

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'result':'success', 'data':serializer.data},
            status=status.HTTP_200_OK)
        else :
            #값이 들어갔는지 응답을 해주기 위해
            return Response({'result':'fail', 'data':serializer.errors}, status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        #누구한테 지정? 했는지 
        if kwargs.get('uid') is None:
            return Response("uid required", status = status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            user_object = User.objects.get(id=uid)
            #request.data는 프론트엔드에서 보내는 데이터고 그거를 user_object로 수정한다는 거임
            serializer = UserSerializer(user_object, data=request.data)
# serializer 변수명이라서 뒤에 var를 붙이면
# serializer = UserSerializer(user_object, data=request.data)


            if serializer.is_valid():
                serializer.save()
                return Response({'result':'success', 'data':serializer.data},
                                status=status.HTTP_200_OK)
            else:
                return Response("uid required", status = status.HTTP_400_BAD_REQUEST)

    def delete(self,reqeust,**kwargs):
        if kwargs.get('uid') is None:
            return Response("uid required", status = status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            user_object = User.objects.get(id=uid)
            user_object.delete()
            return Response({"result":"success"}, status= status.HTTP_200_OK)