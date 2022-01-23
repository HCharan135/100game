# my view of the pagep
from django.http import HttpResponse
from django.shortcuts import render
import random

def index(request):
    return render(request, "index.html")


def rules(request):
    return render(request,'rules.html')


def result(request,):


    sum = int(0 if request.GET.get('punc') is None else request.GET.get('punc'))
    num = int(0 if request.GET.get('numbertoadd') is None else request.GET.get('numbertoadd'))
    mysum = sum + num
    sum=sum+num
    if mysum>100:
        return render(request,'result.html')
    if mysum==100:
        return render(request,'win.html')
    if sum<35:
        random1=random.randint(1,10)
        sum = sum + random1
        params = {'purpose': 'Extra space removed ', 'num': num, 'sum': sum, 'random1': random1,'mysum':mysum}
        return render(request, 'index.html', params)
    else:
        list=[1,12,23,34,45,56,67,78,89,100]
        for i in list:
            if sum < i:
                print("adfasef", i,sum)
                random1= i-sum
                if random1>10:
                    random1=random.randint(1,10)
                print(random1)
                break
        sum = sum + random1
        if sum==100:
            params = {'purpose': 'Extra space removed ', 'num': num, 'sum': sum, 'random1': random1, 'mysum': mysum}
            return render(request, 'lose.html',params)

    params = {'purpose': 'Extra space removed ', 'num': num, 'sum': sum, 'random1': random1,'mysum':mysum}
    return render(request,'index.html', params)
