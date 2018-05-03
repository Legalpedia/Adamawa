from imports import *


def updates(request):
    template = loader.get_template('manager_listupdates.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def newupdate(request):
    template = loader.get_template('manager_newupdates.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))
