from imports import *
from tasks import *

def laws(request):
    template = loader.get_template('manager_laws_view.html')
    laws=Laws.objects.order_by('title').all()
    datalist=lawsviewToJson(laws)
    data['laws']=datalist
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def laws_main(request):
    template = loader.get_template('manager_laws_view_main.html')
    laws=Laws.objects.order_by('title').all()
    datalist=lawsviewToJson(laws)
    data['laws']=datalist
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def createlaw(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        title=request.POST.get('title')
        lawnumber=request.POST.get('number')
        lawdate=request.POST.get('lawdate')
        lawdesc=request.POST.get('lawdesc')
        try:
            resource=Laws.objects.create(title=title,number=lawnumber,date=lawdate,description=lawdesc,postdate=timezone.now(),updatedate=timezone.now())
            request.session['message']= "ok"
        except Exception as ex:
            request.session['message']= "failed"
        return HttpResponseRedirect("laws")
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")


def createsection(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        lawid=request.POST.get('title')
        partschedule=request.POST.get('schedule')
        title=request.POST.get('heading')
        body=request.POST.get('lawdesc')
        try:
            resource=Sections.objects.create(lawid=lawid,partschedule=partschedule,title=title,body=body,postdate=timezone.now(),updatedate=timezone.now())
            request.session['message']= "ok"
        except Exception as ex:
            request.session['message']= "failed"
        return HttpResponseRedirect("laws_upload")
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")



def uploadlaws(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        requests={}
        requests['files']=request.FILES.getlist('files')
        doUpload.delay(requests)
        return HttpResponseRedirect("laws")
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")


def listlaws(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        offset=request.GET['offset']
        limit=request.GET['limit']
        pager="LIMIT "+offset+","+limit
        laws=Laws.objects.raw("SELECT  a.id as id,a.title as title from api_laws a "+pager)
        data={}
        data['total']= Laws.objects.count()
        data['rows']=lawdataToJson(laws)
        return JsonResponse(data)
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")


def listsections(request,id):
    if request.session.get('ismanagerloggedin', False):
        print "List sections"
        data={}
        if not id:
            id=request.GET['id']
        offset=request.GET['offset']
        limit=request.GET['limit']
        pager="LIMIT "+offset+","+limit
        sections=Laws.objects.raw("SELECT  b.id as id,b.title as title,b.body as body from api_laws a,api_sections b WHERE b.lawid=a.id and a.id="+id+" "+pager)
        data={}
        data['total']= len(list(Laws.objects.raw("SELECT  b.id as id,b.title as title,b.body as body from api_laws a,api_sections b WHERE b.lawid=a.id and a.id="+id)))
        data['rows']=sectiondataToJson(sections)
        return JsonResponse(data)
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")