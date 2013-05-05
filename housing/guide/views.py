from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
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
            geojson['properties'] = properties
            d[shape.osm_id] = geojson
        return HttpResponse(json.dumps(d), mimetype='application/json')

    return render_to_response('test.html')
