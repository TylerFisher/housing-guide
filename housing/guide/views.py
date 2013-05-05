from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

from guide.models import *

def ensure_get(request):
    """Ensure that a view function was called via a GET request"""
    if request.method != 'GET':
        raise Http404

def home(request):

    ensure_get(request)

    shapes = DormShapes.objects.all().order_by('name')

    return render_to_response('test.html', {
            'shapes': shapes
        })
