from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

from django.views.decorators.csrf import csrf_exempt
from .models import User
# Create your views here.
import json, base64

import urllib.parse

@csrf_exempt
def getting_user_info(request):
	if request.method=='POST':
		json_obj = json.loads(request.body)		
		raw = User.objects.create(user_id=json_obj['user_id'], first_name = json_obj['first_name'], 
			img_url = json_obj['img_url'], last_name = json_obj['last_name'])
		raw.save()
		return StreamingHttpResponse('it was post request: ')
	else:
		return StreamingHttpResponse('it was GET request')

@csrf_exempt
def display_users(request):
	user_info = User.objects.all()
	print(user_info)
	return render(request, "index.html", {"user":user_info})

def update_user_page(request):
	
	user_info = User.objects.all()
	response_data = {}
	response_object = []
	for i in user_info:

		response_data['user_id'] = i.user_id
		response_data['first_name'] = i.first_name
		response_data['last_name'] = i.last_name
		response_data['img_url'] = i.img_url
		response_object.append(response_data.copy())
	print(response_object)
	
	return HttpResponse(json.dumps(response_object), content_type = "aplication/json")


def parse_user_json(json_obj):
	#decoding
	pass
