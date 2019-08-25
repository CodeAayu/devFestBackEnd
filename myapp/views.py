import json, datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from myapp.models import gitnoti
# Create your views here.

@csrf_exempt
def notification(request):
	data = json.loads(json.dumps(request.POST.dict()))
	data = json.loads(data['payload'])
	#print(data)
	try:
		action = data['action']
	except:
		try:
			action = data['commits'][0]['message']
		except:
			action = str("Pull request of reference : " + data['ref'])
	repo_name = data['repository']['name']
	repo_url = data['repository']['html_url']
	sender_name = data['sender']['login']
	sender_url = data['sender']['html_url']
	gitnoti.objects.create(action=action,repo_name=repo_name,repo_url=repo_url,sender_name=sender_name,sender_url=sender_url)
	obj = list(gitnoti.objects.all().values())
	if len(obj) == 16:
		gitnoti.objects.get(id=obj[0]['id']).delete()
	return HttpResponse("Done!")

@csrf_exempt
def apiendpoint(request):
	if request.method == 'GET':
		data = gitnoti.objects.all().values()
		listing = list(data)
		return JsonResponse(listing, safe=False)
	return HttpResponse("Wrong Request!")