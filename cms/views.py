from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard(request):
    return render(request, 'cms/dashboard.html')


def contests(request):
	return render_to_response('cms/contests.html', {'title': 'Contests'}, context_instance=RequestContext(request))
    # return render(request, 'cms/contests.html')


def promos(request):
    return render(request, 'cms/promos.html')


def newsfeeds(request):
    return render(request, 'cms/newsfeeds.html')