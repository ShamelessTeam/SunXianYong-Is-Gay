from api import models
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    # 文章序列化
    source = serializers.CharField(source='source.name')
    class Meta:
        model = models.Article
        # fields = '__all__'
        fields = ['title','source','brief','comment_num','agree_num','view_num','collect_num']


class ArticleDetailSerializer(serializers.ModelSerializer):
    # 文章详细序列化
    article_type = serializers.CharField(source='get_article_type_display')
    status = serializers.CharField(source='get_status_display')
    position = serializers.CharField(source='get_position_display')
    # m2m
    class Meta:
        model = models.Article
        fields = ['title','source','article_type','head_img','content','pub_date','offline_date',
                  'status','order','vid','comment_num','agree_num','view_num','collect_num','date',
                  'position']
    #
    # def get_recommends(self,obj):
    #     # 获取推荐的所有课程
    #     queryset = obj.recommend_courses.all()
    #     return [{'id':row.id,'title':row.name} for row in queryset]
    #
    # def get_teachers(self, obj):
    #     queryset = obj.teachers.all()
    #     return [{'id':row.id,'name':row.name} for row in queryset]
