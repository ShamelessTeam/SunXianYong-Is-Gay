"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from study.views import course
from study.views import account

urlpatterns = [
    url(r'^degreecourse/$', course.DegreeCourseView.as_view({'get': 'list'})),
    url(r'^degreecourse/(?P<pk>\d+)/$', course.DegreeCourseView.as_view({'get': 'retrieve'})),
    url(r'^coursecategory/$', course.CourseCategoryView.as_view({'get': 'list'})),
    url(r'^coursecategory/(?P<pk>\d+)/$', course.CourseCategoryView.as_view({'get': 'retrieve'})),
    url(r'^course/$', course.CourseView.as_view({'get': 'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retrieve'})),
    url(r'^article/$', course.ArticleView.as_view({'get': 'list'})),
    url(r'^article/(?P<pk>\d+)/$', course.ArticleView.as_view({'get': 'retrieve'})),
    # url(r'^auth/$', account.AuthView.as_view()),
    # url(r'^micro/$', course.MicroView.as_view()),
]
