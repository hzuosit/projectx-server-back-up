from django.shortcuts import render
from django.http import HttpResponse
from arcadia.models import CustomerInfo,RelationInfo,TempInfo,HumInfo,CO1Info,MoInfo,DeviceBook
import json
from django.db.models import Avg,Max,Count,Min,Sum
from django.utils import timezone

import json
# Create your views here.
# Here includes some test funtions and data handling functions.
def test(request):
    if request.method=="POST":
        if request.META['HTTP_PI']=='TEST':
            #a=json.loads(request.body)
            aa=CustomerInfo.objects.filter(id=1)
            return HttpResponse(aa)
        else:
            return HttpResponse("need a proper header file")
        
        return HttpResponse("Post works")
    return HttpResponse("it's a 'get' request")

def mytest(request):
    if request.method=="POST":
        
        if request.META['HTTP_PI']=='CZL':
            buff=json.loads(request.body)
            
            if DeviceBook.objects.filter(address=buff['address']).exists():
                DeviceBook.objects.get(address=buff['address']).status=True
                DeviceBook.objects.get(address=buff['address']).value=='TEMP'
                return HttpResponse("this part works")
            else:
                return HttpResponse("this part doesn't work")
            
            return HttpResponse(buff['address'])
        else:
            return HttpResponse("need a proper header file")
        
        

    return HttpResponse("it's a 'get' request")
    

def DataIn(request):
    if request.method=='POST':
        if request.META['HTTP_PI']=='CZL':
            buff=json.loads(request.body)

            if DeviceBook.objects.filter(address=buff['address']).exists():
                DeviceBook.objects.get(address=buff['address']).status=True

                if DeviceBook.objects.get(address=buff['address']).value=='TEMP':
                    users=DeviceBook.objects.get(address=buff['address'])
                    BUFF=TempInfo(temperature=(buff['value']-500)/10,user=users)
                    #BUFF=TempInfo(temperature=buff['value'],user=users)
                    BUFF.save()
                    return HttpResponse("OK")

                elif DeviceBook.objects.get(address=buff['address']).value=='HUM':
                    users=DeviceBook.objects.get(address=buff['address'])
                    BUFF=HumInfo(humidity=buff['value'])
                    BUFF.save()
                    return HttpResponse("OK")

                elif DeviceBook.objects.get(address=buff['address']).value=='CO1':
                    users=DeviceBook.objects.get(address=buff['address'])
                    BUFF=CO1Info(CO1=buff['value'])
                    BUFF.save()
                    return HttpResponse("OK")

                elif DeviceBook.objects.get(address=buff['address']).value=='MO':
                    users=DeviceBook.objects.get(address=buff['address'])
                    BUFF=MoInfo(motion=buff['value'],user=users)
                    BUFF.save()
                    return HttpResponse("OK")

            else:
                return HttpResponse("device not exist")

        else: 
            return HttpResponse("wrong input")
    else:
        return HttpResponse("Incorrect Request")

def DataInput(request):
        ## API only for post ##
    if request.method=="POST":
        ## data input followed by different headers ##
        ## temperature info ##
        if request.META['HTTP_PI']=='TEMP':
            buff=json.loads(request.body)
            ## logical calculation ##
            ## relational linking information##
            ## date and time ##
            ##BUFF=TempInfo("temperature ,device and date time, auth block")
            BUFF=TempInfo(temperature=buff['value'])
            BUFF.save()
            return HttpResponse("OK")
        ## humidity info ##
        elif request.META['HTTP_PI']=='HUM':
            buff=json.loads(request.body)
            ## logical calculation ##
            ## relational linking information##
            ## date and time ##
            ##BUFF=HumInfo("humidity ,device and date time, auth block")
            BUFF=HumInfo(humidity=buff['value'])
            BUFF.save()
            return HttpResponse("OK")
        ## CO1 info ##
        elif request.META['HTTP_PI']=='CO1':
            buff=json.loads(request.body)
            ## logical calculation ##
            ## relational linking information##
            ## date and time ##
            ##BUFF=CO1Info("CO1 ,device and date time, auth block")
            BUFF=CO1Info(CO1=buff['value'])
            BUFF.save()
            return HttpResponse("OK")
        else:
            return HttpResponse("wrong input")
    else:
        return HttpResponse("Incorrect request") 

    
## func to handle temperature info reqeusts ##
def TempRequest(request):
    if request.method=='POST':
        if request.META['HTTP_TEMP']=='LATEST':
            BUFF=TempInfo.objects.last()
            return HttpResponse(str(BUFF.temperature))
        elif request.META['HTTP_TEMP']=='HIGHEST':
            BUFF=TempInfo.objects.all().aggregate(Max('temperature'))
            return HttpResponse(BUFF['temperature__max'])
        elif request.META['HTTP_TEMP']=='LOWEST':
            BUFF=TempInfo.objects.all().aggregate(Min('temperature'))
            return HttpResponse(BUFF['temperature__min'])
        else:
            return HttpResponse("wrong Temperature request")
    else:
        return HttpResponse("Incorrect request")

## func of new temp requests
def TempRequests(request):
    if request.method=='POST':
        if request.META['HTTP_TEMP']=='LATEST':
            buff=json.loads(request.body)
            users=DeviceBook.objects.get(address=buff['address'])
            BUFF=TempInfo.objects.all().filter(user=users).last()
            return HttpResponse(str(BUFF.temperature))
        elif request.META['HTTP_TEMP']=='HIGHEST':
            buff=json.loads(request.body)
            users=DeviceBook.objects.get(address=buff['address'])
            BUFF=TempInfo.objects.all().filter(user=users).aggregate(Max('temperature'))
            return HttpResponse(BUFF['temperature__max'])
        elif request.META['HTTP_TEMP']=='LOWEST':
            buff=json.loads(request.body)
            users=DeviceBook.objects.get(address=buff['address'])
            BUFF=TempInfo.objects.all().filter(user=users).aggregate(Min('temperature'))
            return HttpResponse(BUFF['temperature__min'])
        else:
            return HttpResponse("wrong Temperature request")
    else:
        return HttpResponse("Incorrect request")

## func of new temp requestss
def TempRequestss(request):
    if request.method=='POST':
        if request.META['HTTP_TEMP']=='LATEST':
            buff=request.META['HTTP_ADDRESS']
            users=DeviceBook.objects.get(address=buff)
            BUFF=TempInfo.objects.all().filter(user=users).last()
            return HttpResponse(str(BUFF.temperature))
        elif request.META['HTTP_TEMP']=='HIGHEST':
            buff=request.META['HTTP_ADDRESS']
            users=DeviceBook.objects.get(address=buff)
            BUFF=TempInfo.objects.all().filter(user=users).aggregate(Max('temperature'))
            return HttpResponse(BUFF['temperature__max'])
        elif request.META['HTTP_TEMP']=='LOWEST':
            buff=request.META['HTTP_ADDRESS']
            users=DeviceBook.objects.get(address=buff)
            BUFF=TempInfo.objects.all().filter(user=users).aggregate(Min('temperature'))
            return HttpResponse(BUFF['temperature__min'])
        else:
            return HttpResponse("wrong Temperature request")
    else:
        return HttpResponse("Incorrect request")
## func to handle humidity info reqeusts ##
def HumRequest(request):
    if request.method=='POST':
        if request.META['HTTP_HUM']=='LATEST':
            buff=request.META['HTTP_ADDRESS']
            users=DeviceBook.objects.get(address=buff)
            BUFF=HumInfo.objects.all().filter(user=users).last()
            return HttpResponse(str(BUFF.humidity))
        elif request.META['HTTP_HUM']=='HIGHEST':
            buff=request.META['HTTP_ADDRESS']
            users=DeviceBook.objects.get(address=buff)
            BUFF=HumInfo.objects.all().filter(user=users).aggregate(Max('humidity'))
            return HttpResponse(BUFF['humidity__max'])
        elif request.META['HTTP_HUM']=='LOWEST':
            buff=request.META['HTTP_ADDRESS']
            users=DeviceBook.objects.get(address=buff)
            BUFF=HumInfo.objects.all().aggregate(Min('humidity'))
            return HttpResponse(BUFF['humidity__min'])
        else:
            return HttpResponse("wrong humidity request")
    else:
        return HttpResponse("Incorrect request")

## func to handle CO1 info reqeusts ##
def CO1Request(request):
    if request.method=='POST':
        if request.META['HTTP_CO']=='LATEST':
            BUFF=CO1Info.objects.latest('time')
            return HttpResponse(str(BUFF.CO1))
        elif request.META['HTTP_CO']=='HIGHEST':
            BUFF=CO1Info.objects.all().aggregate(Max('CO1'))
            return HttpResponse(BUFF['CO1__max'])
        elif request.META['HTTP_CO']=='LOWEST':
            BUFF=CO1Info.objects.all().aggregate(Min('CO1'))
            return HttpResponse(BUFF['CO1__min'])
        else:
            return HttpResponse("wrong CO1 request")
    else:
        return HttpResponse("Incorrect request")

## func to handle MO info requests ##
def MoRequest(request):
    if request.method=='POST':
        if request.META['HTTP_MO']=='LATEST':
            buff=request.META['HTTP_ADDRESS']
            users=DeviceBook.objects.get(address=buff)
            BUFF=MoInfo.objects.all().filter(user=users).last()
            return HttpResponse(str(BUFF.motion))
        else:
            return HttpResponse("wrong Motion request")
    else:
        return HttpResponse("Incorrect request")

## func for http get request ##
def TempNow(request):
    if request.method=='GET':
        BUFF=TempInfo.objects.latest('time')
        return HttpResponse(str(BUFF.temperature))
    return HttpResponse("error")
