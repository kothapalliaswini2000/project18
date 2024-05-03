from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
def insert_topic(request):
    tn=input('enter name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    d={'QLTO':Topic.objects.all()}
    return render(request,'display_topics.html',d)

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
        d={'QLWO':Webpage.objects.all()}
        return render(request,'display_webpage.html',d)
    else:
        return HttpResponse('ypur data is not sufficient')

def insert_AccessRecord(request):
    i=int(input('enter id of webpage object'))

    WO=Webpage.objects.get(id=i)
    d=input('enter date')
    a=input('enter author')
    
    
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    return HttpResponse('AccessRecord is created')

def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',context=d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='cricket')
    QLWO=Webpage.objects.exclude(topic_name='cricket')
    #QLWO=Webpage.objects.get(topic_name='Football')#here,it will throw error,y becouse get() will gives objects directly
    QLWO=Webpage.objects.all()[:3:]
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.filter(name__startswith='a')
    QLWO=Webpage.objects.filter(name__startswith='a')
    QLWO=Webpage.objects.filter(name__endswith='i')
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(email__endswith='com')
    QLWO=Webpage.objects.filter(url__endswith='in')
    QLWO=Webpage.objects.filter(name__contains='h')
    QLWO=Webpage.objects.filter(name__in=['aswini'])
    QLWO=Webpage.objects.filter(name__in=['aswini','kohli'])

    
    



    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',context=d)

def display_AccessRecords(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__year='2024')
    QLAO=AccessRecord.objects.filter(date__month='04')
    QLAO=AccessRecord.objects.filter(date__day='7')
    QLAO=AccessRecord.objects.filter(date__year__gte='2000')
    QLAO=AccessRecord.objects.filter(date__year__gt='2000')
    QLAO=AccessRecord.objects.filter(date__year__lte='2000')
    QLAO=AccessRecord.objects.filter(date__year__lt='2000')

    d={'QLAO':QLAO}
    return render(request,'display_AccessRecords.html',context=d)



