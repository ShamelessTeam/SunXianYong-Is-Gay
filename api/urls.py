from django.conf.urls import url,include
from django.contrib import admin
from api.views.course import CourseView
from api.views.article import ArticleView

urlpatterns = [
    url(r'^course/$', CourseView.CourseViewSet.as_view({"get": "list"})),
    url(r'^course/(?P<pk>\d+)/$', CourseView.CourseViewSet.as_view({"get": "retrieve"})),
    url('article/$', ArticleView.ArticleView.as_view({'get':'list'})),
    url('article/(?P<pk>\d+)', ArticleView.ArticleView.as_view({'get':'retrieve'})),
]

