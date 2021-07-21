from json.encoder import JSONEncoder
from os import stat
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import time
import json
from . import userfunc 

# Create your views here.
WORKERS = {}
# API_KEYS = {"dTb4j877t7rdgwkjM2D8wcgr6mdaSzuvt3h8j2fA8tLxg2h48q":0}
API_KEYS = {"0":0,"5":5}
LAST_UPDATE = {}
def index(request):
    context={"title":"Dashboard", "dash_class":"active", "logs_class":"", "att_class":"","about_class":""}
    return render(request, 'index.html', context)

def attendence(request):
    context={"title":"Dashboard", "dash_class":"", "logs_class":"", "att_class":"active","about_class":""}
    return render(request, 'attendance.html',context)

def logs(request):
    context={"title":"Dashboard", "dash_class":"", "logs_class":"active", "att_class":"","about_class":""}
    return render(request, 'attendance.html',context)

def about(request):
    context={"title":"Dashboard", "dash_class":"", "logs_class":"", "att_class":"","about_class":"active"}
    return render(request, 'about.html',context)

@csrf_exempt
def get(request):
    global WORKERS
    global LAST_UPDATE
    response_val = {}
    if(request.method == "GET"):
        if(request.GET.get("addr")):
            address_val = request.GET['addr']
            if(request.GET['addr']=='all'):
                response_val, LAST_UPDATE = userfunc.update_dashboard(WORKERS, LAST_UPDATE)
            elif request.GET['addr'] in WORKERS:
                print(WORKERS)
                response_val = WORKERS[str(address_val)]
    return JsonResponse(response_val)
    

@csrf_exempt
def send(request):
    global WORKERS
    status = "[ERROR]"
    json_body = {}
    if(request.method == "POST"):
        body_raw = request.body
        json_body = json.loads(body_raw)
        if("addr" in json_body) and ("data" in json_body):
            status = "[OK]"
            address_val = json_body["addr"]
            if address_val not in API_KEYS:
                json_body="Invalid API KEY"
            else:
                WORKERS[API_KEYS[address_val]] = json_body["data"]
                LAST_UPDATE[API_KEYS[address_val]] = int(time.time())
        else:
            json_body = "Invalid Request"
        print(json_body)
    return JsonResponse({"status":status, "reponse": json_body})
    