from django.conf.urls import url
from . import views

app_name = 'startsurvey'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^(?P<test_id>[0-9])/$', views.vote, name="vote"),
    url(r'^(?P<test_id>[0-9])/$', views.start, name="start"),
    # url(r'^(?P<test_id>[0-9])/result/$', views.result, name="result"),
]