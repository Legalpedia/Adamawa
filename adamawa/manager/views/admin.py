from imports import *


def listadmin(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        offset=request.GET['offset']
        limit=request.GET['limit']
        pager="LIMIT "+offset+","+limit
        admin=Admin.objects.raw("SELECT  api_admin.id as id,api_adminrole.name as role,username,status from api_admin,api_adminrole WHERE api_admin.role=api_adminrole.id "+pager)
        data={}
        data['total']= Admin.objects.count()
        data['rows']=adminToJson(admin)
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")