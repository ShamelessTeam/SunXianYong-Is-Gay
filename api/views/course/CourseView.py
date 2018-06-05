from api.models import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from api.serializers.CourseView import *


# Create your views here.

class CourseViewSet(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        """
        课程主页显示资源
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Course.objects.all()
            ser = CourseViewSetSerializers(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '未获取到资源'
        complate_data = Response(ret)
        print(complate_data)
        return complate_data

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        print('----------------测试开始--------------')

        print('----------------测试结束--------------')
        try:
            pk = kwargs.get('pk')
            obj = CourseDetail.objects.filter(id=pk).first()
            ser = CourseDetailViewSetSerializers(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '未获取到资源'
        complate_data = Response(ret)
        print(complate_data)
        return complate_data

