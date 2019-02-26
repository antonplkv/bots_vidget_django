from django.http import HttpResponse
def hello(request):
	print()
	print(request)
	print(dir(request))
	return HttpResponse("<b>XUI</b>")