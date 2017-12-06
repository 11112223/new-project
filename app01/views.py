from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):  #这边发送



    return render(request,'index.html')