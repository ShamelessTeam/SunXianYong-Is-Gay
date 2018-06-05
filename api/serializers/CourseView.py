from rest_framework import serializers
from api.models import *


class CourseViewSetSerializers(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    why_studys = serializers.CharField(source='coursedetail.why_study')

    class Meta:
        model = Course
        fields = ['name', 'course_img', 'level', 'template_id', 'why_studys']


class CourseDetailViewSetSerializers(serializers.ModelSerializer):
    # oto fenkey
    name = serializers.CharField(source='course.name')
    course_type = serializers.CharField(source='course.get_course_type_display')
    period = serializers.CharField(source='course.period')
    level = serializers.CharField(source='course.get_level_display')
    template_id = serializers.CharField(source='course.template_id')
    # mtm
    recommend_courses = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()
    courseoutlines = serializers.SerializerMethodField()
    oftenAskedquestions = serializers.SerializerMethodField()
    pricepolicy = serializers.SerializerMethodField()

    class Meta:
        model = CourseDetail
        fields = ['name', 'course_type', 'period', 'level', 'template_id', 'video_brief_link', 'why_study',
                  'what_to_study_brief', 'career_improvement', 'prerequisite', 'recommend_courses', 'teachers',
                  'courseoutlines', 'oftenAskedquestions', 'pricepolicy']

    def get_recommend_courses(self, obj):
        queryset = obj.recommend_courses.all()
        return [{'name': item.name} for item in queryset]

    def get_teachers(self, obj):
        queryset = obj.teachers.all()
        return [{'name': item.name, 'title': item.title, 'signature': item.signature, 'image': item.image,
                 'brief': item.brief, 'role': item.role} for item in queryset]

    def get_courseoutlines(self, obj):
        queryset = obj.courseoutline_set.all()
        return [{'title': item.title, 'content': item.content} for item in queryset]

    def get_oftenAskedquestions(self, obj):
        queryset = obj.course.asked_question.all()
        return [{'question': item.question, 'answer': item.answer} for item in queryset]

    def get_pricepolicy(self, obj):
        queryset = obj.course.price_policy.all()
        return [{'price': item.price, 'valid_period': item.valid_period} for item in queryset]
