from django.shortcuts import render
from django.http import HttpResponse
import paho.mqtt.client as mqtt
import time
import json
from django.http import JsonResponse
from createmodels.models import sensors
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import paho.mqtt.publish as mqttpublish

mqttBroker = "broker.hivemq.com"
client=mqtt.Client("Testing")
client.connect(mqttBroker)

def on_message(client, userdata, message):
    _decode = str(message.payload.decode("utf-8"))
    new = json.loads(_decode)
    print(new) 
    Temp = new["Temperature"] 
    Humid = new["Humidity"] 
    Moist = new["Moisture"] 
    Date = timezone.now()
    Sensor = sensors(Temperature = Temp, Humidity = Humid, Moisturelvl = Moist, DataDate = Date)
    Sensor.save()

def showreadings(request):
    data = {"data":[]}
    if request.method == 'GET':
        readings = sensors.objects.all().order_by('-id')[0]
        context = {
        "Temperature": readings.Temperature,
        "Humidity": readings.Humidity,
        "MoistureLevel": readings.Moisturelvl,
        "Date": readings.DataDate
        }
        data["data"].append(context)
    return JsonResponse(data)

@method_decorator(csrf_exempt)
@csrf_exempt

def control(request):
    data = {"data":[]}
    if request.method == 'POST':
        context = {
            "ID" : request.POST.get("ActuatorID"),
            "state" : request.POST.get("Value")
        }
        data["data"].append(context)
        print("updated data is...", data)
        mqttpublish.single("Actuator", payload=json.dumps(data), qos=0, retain=False, hostname="broker.hivemq.com", port=1883, keepalive=60)
    return JsonResponse(data)

def homepage(request):
    return render(request, 'Datapage/Homepage.html')

client.loop_start()
client.subscribe("Compostbin")
client.on_message = on_message
time.sleep(30)
client.loop_stop

#Create your views here.

