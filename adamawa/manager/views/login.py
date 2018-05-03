from imports import *


def auth(request):
    if request.method == "POST":
            username=request.POST.get("username")
            passwd=request.POST.get("password")
            password=hashlib.sha256(passwd).hexdigest()
            try:
                admin=Admin.objects.filter(Q(username=username) & Q(password=password)).get()
                if admin.username!=None:
                    data={}
                    request.session['ismanagerloggedin']=True
                    request.session['username']=username
                    request.session['uid']=admin.id
                    request.session['role']=admin.role
                    return HttpResponseRedirect("/manager")

                else:
                    request.session['message']="Invalid username/password pair"
                    request.session['ismanagerloggedin']=False
                    return HttpResponseRedirect("login")
            except Exception as ex:
                request.session['message']="Invalid username/password pair"
                request.session['ismanagerloggedin']=False
                return HttpResponseRedirect("login")



    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")




def login(request):
    data['message']=None
    if "message" in request.session:
        data['message']=request.session['message']
        del request.session['message']
    template = loader.get_template('manager_login.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    request.session.modified = True
    return HttpResponseRedirect("login")