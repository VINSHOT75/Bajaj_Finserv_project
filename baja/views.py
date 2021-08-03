from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

@csrf_exempt 
def splitevenodd(A): 
    evenlist = [] 
    oddlist = [] 
    for i in A:
        if type(i)==type("abc"):
            return "abc","abc"
        else:
            if (i % 2 == 0): 
                evenlist.append(i) 
            else: 
                oddlist.append(i) 
    return evenlist,oddlist
# Create your views here.
@csrf_exempt 
def baja(request):
    if request.method == "POST":
        body = json.loads(request.body)
        lst = list(body["numbers"])
        even,odd = splitevenodd(lst)
        if even!="abc":
            res = {
                "is_success" : True,
                "user_id":"john_doe_17091999",
                "even" : even,
                "odd" : odd,
                }
        else:
            res = {
                "is_success" : False,
                "user_id":"john_doe_17091999",
                }
    return JsonResponse(res)