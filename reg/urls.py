from django.conf.urls import url, include
from . import views

app_name = 'reg'
urlpatterns = [
    url(r'^$', views.RegisterForm.as_view(), name="reg"),
    url(r'^profile/', views.update_profile, name='profile'),
    url(r'^login/', views.AuthForm.as_view(), name='login'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^check/', views.check, name='check'),
]