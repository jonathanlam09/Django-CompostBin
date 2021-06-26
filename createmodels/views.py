from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from pandas.io import pickle
from .models import sensors

def predict(request):
    data = {"data":[]}
    if request.method == 'GET':
        Temperature = sensors.objects.all().order_by('-id')[0].Temperature
        Moisture_Level = sensors.objects.all().order_by('-id')[0].Moisturelvl
        Startdate = sensors.objects.all().order_by('id')[0].DataDate
        Enddate = sensors.objects.all().order_by('-id')[0].DataDate
        Format = Enddate - Startdate
        Composted_Time = Format.days

        model = pd.read_pickle(r"D:\Django\FYP\createmodels\model\updated_model.pickle")
        
        result = model.predict([[Temperature, Moisture_Level, Composted_Time]])

        State_Of_Completion = result[0]

        context = {
            "Temperature" : Temperature,
            "Moisture" : Moisture_Level,
            "Time" : Composted_Time,
            "State Of Completion": State_Of_Completion
        }
        data["data"].append(context)

        print("Temperature: ", Temperature,"°C")
        print("Moisture Level: ", Moisture_Level,"%")
        print("Composted Time:", Composted_Time, "days")
        print(State_Of_Completion)
    return JsonResponse(data)

def ready(request):
    if request.method == 'GET':
        return HttpResponse(request, 'testing.html')
