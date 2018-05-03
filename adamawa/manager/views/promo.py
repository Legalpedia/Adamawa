from imports import *

def promo(request):
    if request.session.get('ismanagerloggedin', False):
        data['username']=request.session.get("username")
        template = loader.get_template('manager_promo.html')
        context = {
        'data': data
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("login")