from django.shortcuts import render

def home(request):
        context = {'ip': request.META.get('REMOTE_ADDR')}
	template = "home.html"
	return render(request, template, context)
