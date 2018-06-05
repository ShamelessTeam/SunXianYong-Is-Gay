from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import *
from datetime import datetime

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
class ArtInfoSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields =['title','content','agree_num','pk']