from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView,Response
from rest_framework.viewsets import ViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import *
from datetime import datetime
from api.serializers.ArticleView import *
# Create your views here.

class ArticleView(ViewSet):

    def list(self,request,*args,**kwargs):
        qset = Article.objects.filter(status=0)
        Course_list = ArtSerializer(instance=qset,many=True)
        Course_dic = {'code': 1000, 'data': Course_list.data}
        return Response(Course_dic)


    def retrieve(self,request,*args,**kwargs):
        ret={'code':1000}
        pk = kwargs.get('pk')
        try:
            obj = Article.objects.filter(pk=int(pk)).first()
            ser = ArtInfoSerializer(instance=obj,many=False)
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret={'code':1001,'error':'获取失败'}
        return Response(ret)

