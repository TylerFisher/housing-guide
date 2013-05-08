from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

import json

from guide.models import *

def ensure_get(request):
    """Ensure that a view function was called via a GET request"""
    if request.method != 'GET':
        raise Http404

def home(request):
    ensure_get(request)
    shapes = DormShapes.objects.all()
    if request.is_ajax():
        d = {}
        for shape in shapes.geojson():
            geojson = json.loads(shape.geojson)
            properties = {'name': shape.name}
            geojson['id'] = shape.osm_id
            d[shape.geojson] = geojson
            geojson['properties'] = properties
        return HttpResponse(json.dumps(d), mimetype='application/json')

    return render_to_response('index.html')

def detail(request):
    return render_to_response('detail.html')
