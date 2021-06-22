# from django.shortcuts import render
# from django.http import HttpResponse
# import paho.mqtt.client as mqtt
# import time
# import json
# from django.http import JsonResponse
# from createmodels.models import sensors
# from django.utils import timezone
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# import paho.mqtt.publish as mqttpublish

# mqttBroker = "broker.hivemq.com"
# client=mqtt.Client("Testing")
# client.connect(mqttBroker)


# @method_decorator(csrf_exempt)
# @csrf_exempt

# def control(request):
#     data = {"data":[]}
#     if request.method == 'POST':
#         context = {
#             "ID" : request.POST.get("ActuatorID"),
#             "state" : request.POST.get("Value")
#         }
#         data["data"].append(context)
#         print("updated data is...", data)
#         mqttpublish.single("Compostbin", payload=json.dumps(data), qos=0, retain=False, hostname="broker.hivemq.com", port=1883, keepalive=60)
#     return JsonResponse(data)

# client.loop_start()
# client.subscribe("Compostbin")
# # time.sleep(30)
# # client.loop_stop
