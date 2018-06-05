from django.conf.urls import url,include

from api.views import course
from api.views import account
from api.views import article


urlpatterns = [
    # 方式一
    # url(r'^course/$', course.CourseView.as_view()),
    # url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view()),

    # 方式二
    url(r'^course/$', course.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)$', course.CourseView.as_view({'get':'retrieve'})),
    # url(r'^auth/$',account.AuthView.as_view()),
    # url(r'^micro/$',course.MicroView.as_view()),
    url(r'^article/$', article.ArticleView.as_view({'get':'list'})),
    url(r'^article/(?P<pk>\d+)$', article.ArticleView.as_view({'get':'retrieve'})),
]
