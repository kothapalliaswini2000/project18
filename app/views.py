from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_topic(request):
    tn=input('enter name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is created successfully')

def insert_Webpage(request):
    tn=input('enter name')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    TO=Topic.objects.get(topic_name=tn)[0]
    if LTO:
        TO=LTO[0]

    
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()
        return HttpResponse('Webpage is created successfully')
    else:
        return HttpResponse('ypur data is not sufficient')

def insert_AccessRecord(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    d=input('enter date')
    a=input('enter author')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse('AccessRecord created successfully')

def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',context=d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',context=d)

def display_AccessRecords(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_AccessRecords.html',context=d)



