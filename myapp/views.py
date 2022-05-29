from django.shortcuts import render,HttpResponse

def index(request):
    # return render(request,'wechat/pages/index/index.wxml')
    return HttpResponse('1')
