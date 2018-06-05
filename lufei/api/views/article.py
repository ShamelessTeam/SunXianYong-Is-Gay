from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api.serializers.course import *
from api.serializers.article import *
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
# from api.auth.auth import LuffyAuth
from django.conf import settings


class ArticleView(ViewSetMixin,APIView):
    # 为空可以让不再做默认的认证
    authentication_classes = []
    def list(self,request,*args,**kwargs):
        """
        文章列表接口
        """
        print(888888888888888888888888888888888)
        ret = {'code':1000,'data':None}
        try:
            queryset = models.Article.objects.all()
            print(11111111,queryset)
            ser = ArticleSerializer(instance=queryset,many=True)
            print(3333333333333,ser)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取文章失败'
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        文章详细接口
        """
        ret = {'code': 1000, 'data': None}
        try:
            # 文章ID=2
            pk = kwargs.get('pk')
            # 文章详细对象
            obj = models.Article.objects.filter(id=pk).first()
            ser = ArticleDetailSerializer(instance=obj,many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取文章失败'

        return Response(ret)
