from api import models
from rest_framework import serializers
class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    class Meta:
        model = models.Course
        fields = ['id','name','course_img','level']

# class CourseDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CourseDetail
#         fields = "__all__"
#         depth = 1 # 0-10


class CourseDetailSerializer(serializers.ModelSerializer):

    # one2one/fk/choice
    title = serializers.CharField(source='course.name')

    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')

    # m2m
    recommends = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ['title','img','level','hours','course_slogan','video_brief_link','why_study',
                  'what_to_study_brief','career_improvement','prerequisite','recommends','teachers']

    def get_recommends(self,obj):
        # 获取推荐的所有课程
        queryset = obj.recommend_courses.all()
        return [{'id':row.id,'title':row.name} for row in queryset]

    def get_teachers(self, obj):
        queryset = obj.teachers.all()
        return [{'id':row.id,'name':row.name} for row in queryset]
