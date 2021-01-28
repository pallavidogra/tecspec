from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
import json
# Create your views here.
def home(request):
  return render(request,'index.html')

def put(request):
  return render(request,'put.html')

@csrf_exempt
def printscreen(request):
	height = request.POST.get('height')
	length = request.POST.get('length')
	quantity = request.POST.get('quantity')

	return JsonResponse({
	  'status': '200',
	  'msg': 'Success'
	})

def auto_search(request):
  if request.is_ajax():
    query = request.GET.get("term", "")
    companies = Objects.objects.filter(comName__icontains=query)
    results = []
    for company in companies:
        place_json = {'comName':0, 'category':0, 'partNum':0,'supplier':0,'uom':0, 'image':0}
        place_json['comName'] = company.comName
        place_json['category'] = company.category
        place_json['partNum'] = company.partNum
        place_json['supplier'] = company.supplier
        place_json['uom'] = company.uom
        place_json['image'] = str(company.image)
        results.append(place_json)
    data = json.dumps(results)
  mimetype = "application/json"
  return HttpResponse(data, mimetype)