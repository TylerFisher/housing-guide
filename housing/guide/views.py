from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

import json

from guide.models import *

def ensure_get(request):
    """Ensure that a view function was called via a GET request"""
    if request.method != 'GET':
        raise Http404

def home(request):
    dorms = Dorm.objects.order_by('short_name')

    return render_to_response('index.html', {
            'dorms': dorms,
        })

def detail(request, dorm_slug):
    dorm = get_object_or_404(Dorm, slug=dorm_slug)

    shapes = DormShapes.objects.all()
    if request.is_ajax():
        d = {}
        for shape in shapes.geojson():
            if shape.name == dorm.name:
                geojson = json.loads(shape.geojson)
                properties = {'name': shape.name}
                geojson['id'] = shape.osm_id
                d[shape.geojson] = geojson
                geojson['properties'] = properties
        return HttpResponse(json.dumps(d), mimetype='application/json')


    return render_to_response('detail.html', { 'dorm': dorm })

def get_shapes(request):
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

