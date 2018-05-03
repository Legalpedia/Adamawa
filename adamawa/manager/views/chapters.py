from imports import *


def laws2(request):
    template = loader.get_template('manager_laws.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def chapters(request):
    template = loader.get_template('manager_chapter.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def chapters(request):
    template = loader.get_template('manager_chapter.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))