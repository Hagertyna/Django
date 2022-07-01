from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello Ethiopia")


def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age"  : age
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')


def mythirdpage(request):
    var = "hello Ethiopia"
    greet = "how are you friends"
    friuts = ["Orange","Apple","Banana"]
    num1,num2 =3,5
    answer= num1 > num2
    print(answer)
    mydictionary ={
        "var" : var,
        "msg" : greet,
        "myfruits" : friuts,
        "num1" : num1,
        "num2" : num2,
        "answer" : answer
    }
    return render(request,'third.html', context=mydictionary)