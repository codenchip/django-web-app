from django.shortcuts import render
from django.http import HttpResponse
from forward.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.views.generic import TemplateView

import numpy as np
import pandas as pd
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sb

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'combine/index.html', context=None)

class PythonDemo(TemplateView):
    # Create your views here.
    def getNums(request):
        n = np.array([2,3,4])
        name1 = "name-1" + str(n[1])
        return HttpResponse('{"name:":'+name1+',"age":31,"city":"New York"}')

    def getAvg(request):
        s1=request.GET.get("val","")
        if len(s1)==0:
            return HttpResponse("none")
        l1=s1.split(',')
        ar=np.array(l1,dtype=int)

        return HttpResponse(str(np.average(ar)))

    def getGraph(request):
        x = np.arange(0,2 * np.pi, 0.01)
        s = np.cos(x)**2
        plt.plot(x,s)

        plt.xlabel('xlabel(X)')
        plt.ylabel('ylabel(y)')
        plt.title('Basic Graph!')
        plt.grid(True)

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def getData(request):
        samp = np.random.randint(100,600,size=(4,5))
        df = pd.DataFrame(samp, index=['alex','danny','lina','david'],columns=['Jan','Feb','Mar','Apr','May'])
        return HttpResponse(df.to_html(classes='table table-bordered'))

    def getSeabornGraph(request):
        file_path = MEDIA_ROOT+"/data/titanic_train.csv"
        df = pd.read_csv(file_path)
        graph = sb.factorplot(x='Survived',hue='Sex',data=df, col='Pclass',kind='count')
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        return response