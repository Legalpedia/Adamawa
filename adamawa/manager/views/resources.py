from imports import *


def resource(request):
    template = loader.get_template('manager_resources.html')
    data['models']= ContentType.objects.all()
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def createresource(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        name=request.GET['name']
        resourcename=request.GET['resourcename']
        description=request.GET['description']
        title=request.GET['title']
        resource=Resource.objects.create(name=name,resourcename=resourcename,description=description,title=title)
        data={}
        data['total']= Resource.objects.count()
        data['rows']=resourceToJson(resource)
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")


def deleteresource(request,id=None):
    if request.session.get('ismanagerloggedin', False):
        data={}
        try:
            resource=Resource.objects.get(id=id)
            resource.delete()
            data['status']="ok"
            data['message']="successfully deleted resource"
        except Exception as ex:
			data['status']="failed"
			data['message']="unable to delete resource"
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")

def listresource(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        offset=request.GET['offset']
        limit=request.GET['limit']
        pager="LIMIT "+offset+","+limit
        resource=Resource.objects.raw("SELECT  * from api_resource "+pager)
        data={}
        data['total']= Resource.objects.count()
        data['rows']=resourceToJson(resource)
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")

def updateresource(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        offset=request.GET['offset']
        limit=request.GET['limit']
        pager="LIMIT "+offset+","+limit
        resource=Resource.objects.raw("SELECT  api_admin.id as id,api_adminrole.name as role,username,status from api_admin,api_adminrole WHERE api_admin.role=api_adminrole.id "+pager)
        data={}
        data['total']= Resource.objects.count()
        data['rows']=resourceToJson(resource)
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")

