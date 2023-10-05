from django.shortcuts import render
from datetime import datetime
# Create your views here.
def built_in_filter(request):
    data='Hai Hello HOW aRe YoU'
    dt=datetime.now()
    cnt=5
    d={'data':data,'dt':dt,'cnt':cnt}
    return render(request,'built_in_filter.html',d)