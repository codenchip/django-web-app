from django.conf.urls import url 
from combine import views
from django.urls import path 
from django.conf.urls.static import static

app_name = 'combine'

urlpatterns=[
    path('',views.HomePageView.as_view(), name='home'),
    path('getnum/',views.PythonDemo.getNums, name='get-num'),
    path('getavg/',views.PythonDemo.getAvg, name='get-avg'),
    path('getgraph/',views.PythonDemo.getGraph, name='get-graph'),
    path('getdata/',views.PythonDemo.getData, name='get-data'),
    path('get-seaborn-graph/',views.PythonDemo.getSeabornGraph, name='get-seaborn-graph'),
]