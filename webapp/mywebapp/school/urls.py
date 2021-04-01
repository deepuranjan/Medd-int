from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^students/(?P<roll_no>.*)$', views.StudentView.as_view(), name='student'),
    url(r'^students$', views.StudentView.as_view(), name='student'),
]