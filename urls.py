from django.conf.urls import url
from app01.views import course,article,account

urlpatterns = [
    url(r'^course/$', course.CourseView.as_view({'get':'list'})),
    url(r'^article/$', article.ArticleView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get':'retrieve'})),
    url(r'^login/$',account.AuthView.as_view()),
	1
<<<<<<< HEAD
	341234234123412341241234
=======
	341234234123412341241234【wertyhuiopuyte‘
]
>>>>>>> hewm
]