from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView,Response
from rest_framework.viewsets import ViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from luffy_main.models import *
from datetime import datetime
# Create your views here.

'''实例化'''


class ArtSerializer(ModelSerializer):
    pub_date =serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields =['pk', 'title', 'head_img', 'brief',
                        'comment_num','agree_num','pub_date']

    def get_pub_date(self, obj):
        tim = obj.pub_date.replace(tzinfo=None)
        n = datetime.now()
        if (n-tim).days:
            return '%s 天前'%((n-tim).days)
        elif (n-tim).seconds >= 60*60:
            return '%s 小时前'%(int(((n-tim).seconds)/(3600)))
        else:
            return '刚刚'


class CourseInfoSerializer(ModelSerializer):
    level = serializers.CharField(source='course.get_level_display')
    title = serializers.CharField(source='course.name')
    img = serializers.CharField(source='course.course_img')
    Friendlinks = serializers.SerializerMethodField()
    class Meta:
        model = CourseDetail
        fields = ['img','Friendlinks','course_slogan',
                  'why_study','level','title']


    def get_Friendlinks(self,obj):
        ret = obj.recommend_courses.all().values('pk', 'name')
        return ret


class ArtInfoSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields =['title','content','agree_num','pk']


class CourseView(ViewSet):
    def list(self,request,*args,**kwargs):
        Course_list = Course.objects.values('pk','name','course_img','level','brief')
        Course_dic = {'code':0000,'data':Course_list}
        return Response(Course_dic)

    def retrieve(self,request,*args,**kwargs):
        ret={'code':0000}
        pk = kwargs.get('pk')
        try:
            obj = CourseDetail.objects.filter(course__pk=int(pk)).first()
            ser =CourseInfoSerializer(instance=obj,many=False)
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret={'code':1001,'error':'获取失败'}
        return Response(ret)

class CourseInfoView(ViewSet):
    def get(self,request,*args,**kwargs):
        pass

class ArticleView(ViewSet):

    def list(self,request,*args,**kwargs):
        qset = Article.objects.filter(status=0)
        Course_list = ArtSerializer(instance=qset,many=True)
        Course_dic = {'code': 0000, 'data': Course_list.data}
        return Response(Course_dic)


    def retrieve(self,request,*args,**kwargs):
        ret={'code':0000}
        pk = kwargs.get('pk')
        try:
            obj = Article.objects.filter(pk=int(pk)).first()
            ser = ArtInfoSerializer(instance=obj,many=False)
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret={'code':1001,'error':'获取失败'}
        return Response(ret)

class ZanView(ViewSet):

    def list(self):
        pass
    def post(self,request,*args,**kwargs):
        pk = request.data.get('pk')
        obj = Article.objects.filter(pk=pk).first()
        obj.agree_num=obj.agree_num+1
        Article.save(obj)
        ret={'code':0000,'data':obj.agree_num}
        return Response(ret)