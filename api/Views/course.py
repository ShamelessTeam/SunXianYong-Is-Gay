from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from api.serializers.course import CourseSerializer, CourseDetailSerializer, ArticleSerializer, ArticleDetailSerializer, CommentSerializer


class CourseView(ViewSetMixin, APIView):

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
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

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
            obj = models.CourseDetail.objects.filter(course_id=pk).first()
            print('obj:',obj)
            print(123)
            ser = CourseDetailSerializer(instance=obj,many=False)
            print("ser:123",ser.data)

            ret['data'] = ser.data
            print('111111111')
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)


class ArticleView(ViewSetMixin, APIView):

    def list(self,request,*args,**kwargs):
        """
        文章列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'data':None}

        try:
            queryset = models.Article.objects.all()
            ser = ArticleSerializer(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取文章失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        """
        文章详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            # 文章ID=2
            pk = kwargs.get('pk')

            # 课程详细对象
            obj = models.Article.objects.filter(id=pk).first()
            # print('obj:', obj)
            # print(123)
            ser = ArticleDetailSerializer(instance=obj, many=False)
            # print("ser:123", ser.data)

            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取文章失败'

        return Response(ret)


class AgreeView(ViewSetMixin, APIView):

    def list(self,request,*args,**kwargs):
        """
        列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def post(self, request, *args, **kwargs):
        """
        点赞
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
		ret = {'code': 1000, 'data': None}
        try:
			pk = kwargs.get('pk')
			obj = models.Article.objects.filter(id=pk).first()
			obj.agree_num = obj.agree_num + 1
			obj.save()
		except Exception as e:
            ret['code'] = 1001
            ret['error'] = '点赞失败'

        ret = {'code':'1000', 'data': obj.agree_num}
        return Response(ret)


class CollectView(ViewSetMixin, APIView):

    def list(self,request,*args,**kwargs):
        """
        列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def post(self, request, *args, **kwargs):
        """
        收藏
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
		ret = {'code': 1000, 'data': None}
        try:
			pk = kwargs.get('pk')
			obj = models.Article.objects.filter(id=pk).first()
			obj.collect_num = obj.collect_num + 1
			obj.save()
		except Exception as e:
            ret['code'] = 1001
            ret['error'] = '收藏失败'

        ret = {'code':'收藏', 'data': obj.collect_num}

        return Response(ret)


class CommentView(ViewSetMixin, APIView):

    def list(self,request,*args,**kwargs):
        """
        评论列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        try:
            pk = kwargs.get('pk')
            queryset = models.Comment.objects.all()
            ser = CommentSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取评论失败'

        return Response(ret)

    def post(self, request, *args, **kwargs):
        """
        评论详情
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
		ret = {'code': 1000, 'data': None}
        try:
			pk = kwargs.get('pk')
			comment = kwargs.get('comment')
			obj = models.Article.objects.filter(id=pk).first()
			obj.comment = comment
			obj.save()
		except Exception as e:
            ret['code'] = 1001
            ret['error'] = '评论失败'
        ret = {'code': '1000', 'data': obj.agree_num}
        # ret = "1111111"
        return Response(ret)




