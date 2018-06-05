from rest_framework.views import APIView
from rest_framework.response import Response
from study import models
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
# from study.serializers.course import CourseSerializer,CourseDetailSerializer
from study.serializers.course import *
from rest_framework.throttling import SimpleRateThrottle
# from study.auth.auth import LuffyAuth


class CourseCategoryView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        """
        课程大类列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'data':None}

        try:
            queryset = models.CourseCategory.objects.all()
            ser = CourseCategorySerialize(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        print(ret)
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        try:
            # 课程ID=2
            pk = kwargs.get('pk')

            # 课程详细对象
            obj = models.CourseSubCategory.objects.filter(category_id=pk).all()

            ser = CourseSubCategorySerialize(instance=obj,many=True)

            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)


class DegreeCourseView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'data':None}

        try:
            queryset = models.DegreeCourse.objects.all()
            ser = DegreeCourseSerialize(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        print(ret)
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        try:
            # 课程ID=2
            pk = kwargs.get('pk')

            # 课程详细对象
            obj = models.DegreeCourse.objects.filter(id=pk).first()

            ser = DegreeCourseSerialize(instance=obj,many=False)

            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)


class CourseView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        ret = {'code':1000,'data':None}
        try:
            queryset = models.Course.objects.all()
            ser = CourseSerialize(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        print(ret)
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            # 课程ID=2
            pk = kwargs.get('pk')
            # 课程详细对象
            obj = models.Course.objects.filter(id=pk).first()
            ser = CourseSerialize(instance=obj,many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        return Response(ret)


class ArticleView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        ret = {'code':1000,'data':None}
        try:
            queryset = models.Article.objects.all()
            ser = ArticleSerialize(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        print(ret)
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            # 课程ID=2
            pk = kwargs.get('pk')
            # 课程详细对象
            obj = models.Article.objects.filter(id=pk).first()
            ser = ArticleSerialize(instance=obj,many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        return Response(ret)
#
# class MicroView(APIView):
#     authentication_classes = [LuffyAuth,]
#
#     def get(self,request,*args,**kwargs):
#         ret = {'code':1000,'title':'微职位'}
#         return Response(ret)









