from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.
def search(request):
    if request.method =='POST':
        get_value=request.POST.get('username', None)
        print(get_value)
        data={}
        data['result']='you made a request'
        # data['value'] =get_value
        return HttpResponse(json.dumps(data),content_type='application json')
    return render(request,'get.html')
