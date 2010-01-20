from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404

from mrmgr.rackit.models import Rack, Machine


def index(request):
    rack_list = Rack.objects.all()
    return render_to_response('index.html', {'rack_list': rack_list})


def showrack(request, rack_id):
    rack = get_object_or_404(Rack, pk=rack_id)

    machine_list = Machine.objects.filter(rack=rack.name).order_by('position')
    return render_to_response('rack.html', {'rack': rack,
                                            'machine_list': machine_list})
