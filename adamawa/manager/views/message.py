from imports import *


def sms(request):
    template = loader.get_template('manager_sms.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def email(request):
    template = loader.get_template('manager_email.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))