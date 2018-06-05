from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Course)
admin.site.register(CourseCategory)
admin.site.register(CourseChapter)
admin.site.register(CourseDetail)
admin.site.register(CourseOutline)
admin.site.register(CourseSubCategory)
admin.site.register(DegreeCourse)
admin.site.register(Teacher)
admin.site.register(Scholarship)
admin.site.register(OftenAskedQuestion)
admin.site.register(CourseSection)
admin.site.register(Homework)
admin.site.register(PricePolicy)
# ----------深科技相关-------------
admin.site.register(ArticleSource)
admin.site.register(Article)
admin.site.register(Collection)
admin.site.register(Comment)
admin.site.register(Account)
admin.site.register(UserAuthToken)
