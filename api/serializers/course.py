from api import models
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    """
    课程序列化
    """
    level = serializers.CharField(source='get_level_display')

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'course_img', 'brief', 'level']


class ArticleSerializer(serializers.ModelSerializer):
    """
    文章列表序列化
    """

    class Meta:
        model = models.Article
        # fields = '__all__'
        fields = ['id', 'title', 'source', 'brief', 'date', 'comment_num', 'agree_num', 'collect_num', 'view_num']


class ArticleDetailSerializer(serializers.ModelSerializer):
    """
    课程详细序列化
    """

    class Meta:
        model = models.Article
        # fields = '__all__'
        fields = ['id', 'title', 'source', 'content', 'date', 'collect_num', 'view_num']


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    课程详细序列化
    """
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
        model = models.CourseDetail
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


# class CourseDetailSerializer(serializers.ModelSerializer):
#     """
#     课程详细序列化
#     """
#     # one2one/fk/choice
#     title = serializers.CharField(source='course.name')
#     img = serializers.CharField(source='course.course_img')
#     level = serializers.CharField(source='course.get_level_display')
#
#     # m2m
#     recommends = serializers.SerializerMethodField()
#     CourseChapter = serializers.SerializerMethodField()
#
#     class Meta:
#         model = models.CourseDetail
#         # fields = '__all__'
#         fields = ['course','title','img','level','video_brief_link','why_study','recommends', 'CourseChapter']
#
#     def get_recommends(self,obj):
#         # 获取推荐的所有课程
#         queryset = obj.recommend_courses.all()
#
#         return [{'id':row.id,'title':row.name} for row in queryset]
#
#     def get_CourseChapter(self,obj):
#         # 获取所有章节
#
#         queryset = obj.course.coursechapters.all()
#         # s=obj.course
#         # print('------',s)
#
#         # d=s.coursechapters.all()
#         # print(d)
#         return [{'id':row.id,'name':row.name} for row in queryset]


class CommentSerializer(serializers.ModelSerializer):
    """
    评论序列化
    """

    class Meta:
        model = models.Comment
        fields = '__all__'
