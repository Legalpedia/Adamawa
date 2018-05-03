from users import *
from login import *
from promo import *
from transactions import *
from updates import *
from admin import *
from packages import *
from resources import *
from message import *
from chapters import *
from laws import *
from documents import *



def index(request):
    if request.session.get('ismanagerloggedin', False):
        data['numusers']=User.objects.count()
        data['numadmin']=Admin.objects.count()
        data['username']=request.session.get("username")
        template = loader.get_template('manager_dashboard.html')
        context = {
        'data': data
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("login")


def editor(request):
    template = loader.get_template('manager_editor.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def tables(request):
    template = loader.get_template('manager_table1.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def tables2(request):
    template = loader.get_template('manager_table2.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def form(request):
    template = loader.get_template('manager_form1.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def form2(request):
    template = loader.get_template('manager_form2.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


