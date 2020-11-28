from django.conf.urls import url 
from hello_world import views

app_name = 'hello_world'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
]