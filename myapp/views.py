from django.shortcuts import render,render_to_response
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from  myapp.models import *

def index(request):
    #render_to_response('index.html',context_instance=RequestContext(request))
    size = Size.objects.filter(active=True)
    material = Material.objects.filter(active=True)
    piping = Piping.objects.filter(active=True)
    accessories = Accessories.objects.filter(active=True)
    return render(request, 'index.html',{'size':size,'material':material,'piping':piping,'accessories':accessories},
                  context_instance=RequestContext(request))