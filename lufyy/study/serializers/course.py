from study import models

from rest_framework import serializers


class CourseCategorySerialize(serializers.ModelSerializer):

    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']


class CourseSubCategorySerialize(serializers.ModelSerializer):
    Category = serializers.CharField(source='category.name')

    class Meta:
        model = models.CourseSubCategory
        fields = ['Category','id','name']


class DegreeCourseSerialize(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['id', 'name', 'course_img', 'brief', 'total_scholarship', 'mentor_compensation_bonus',
                  'period', 'prerequisite', 'teachers']

    def get_teachers(self, obj):
        # 获取推荐的所有课程
        queryset = obj.teachers.all()
        return [{'id':row.id, 'name':row.name} for row in queryset]


class CourseSerialize(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'course_img', 'sub_category', 'course_type',
                  'degree_course', 'brief','level','pub_date','period','order',
                  'attachment_path','status','template_id']


class ArticleSerialize(serializers.ModelSerializer):
    source = serializers.CharField(source='source.name')
    article_type = serializers.CharField(source='get_article_type_display')
    status = serializers.CharField(source='get_status_display')
    class Meta:
        model = models.Article
        fields = ['id', 'title', 'source', 'article_type', 'brief',
                  'head_img', 'content','pub_date','offline_date','status','order',
                  'vid','comment_num','agree_num','view_num','collect_num','date','position']


#
# class CourseSerializer(serializers.ModelSerializer):
#     """
#     课程序列化
#     """
#     level = serializers.CharField(source='get_level_display')
#
#     class Meta:
#         model = models.Course
#         fields = ['id','title','course_img','level']
#
#
# class CourseDetailSerializer(serializers.ModelSerializer):
#     """
#     课程详细序列化
#     """
#     # one2one/fk/choice
#     title = serializers.CharField(source='course.title')
#     img = serializers.CharField(source='course.course_img')
#     level = serializers.CharField(source='course.get_level_display')
#
#
#     # m2m
#     recommends = serializers.SerializerMethodField()
#     chapter = serializers.SerializerMethodField()
#
#
#     class Meta:
#         model = models.CourseDetail
#         fields = ['course','title','img','level','slogon','why','recommends','chapter']
#
#
#     def get_recommends(self,obj):
#         # 获取推荐的所有课程
#         queryset = obj.recommend_courses.all()
#
#         return [{'id':row.id,'title':row.title} for row in queryset]
#
#     def get_chapter(self,obj):
#         # 获取推荐的所有课程
#         queryset = obj.course.chapter_set.all()
#
#         return [{'id':row.id,'name':row.name} for row in queryset]