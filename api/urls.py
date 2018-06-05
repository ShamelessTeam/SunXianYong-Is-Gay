"""Video_online URL Configuration
    二级路由

"""

from django.conf.urls import url
from api.Views import course

urlpatterns = [
    url(r'^course/$', course.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get':'retrieve'})),


    url(r'^article/$', course.ArticleView.as_view({'get': 'list'})),
    url(r'^article/(?P<pk>\d+)/$', course.ArticleView.as_view({'get': 'retrieve'})),

    url(r'^article/(?P<pk>\d+)/agree/$', course.AgreeView.as_view({'post': 'post'})),

    url(r'^article/(?P<pk>\d+)/collect/$', course.CollectView.as_view({'post': 'post'})),

    url(r'^article/(?P<pk>\d+)/comment/$', course.CommentView.as_view({'post': 'post'})),
    url(r'^comment/$', course.CommentView.as_view({'get': 'list', 'post': 'post'})),


]


