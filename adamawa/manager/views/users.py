from imports import *


def users(request):
    if request.session.get('ismanagerloggedin', False):
        print request.GET.get("action")
        if request.GET.get("action")!=None:
            action=request.GET.get("action")
            if action=="edit":
                uid=request.GET.get("uid")
                user=User.objects.get(id=uid)
                profile=Profile.objects.get(uid=uid)
                userdata={}
                userdata['id']=user.id
                userdata['username']=user.username
                userdata['firstname']=profile.firstname
                userdata['lastname']=profile.lastname
                userdata['phone']=profile.phone
                userdata['email']=profile.email
                userdata['skype']=profile.skype
                userdata['address1']=profile.address1
                userdata['address2']=profile.address2
                userdata['city']=profile.city
                userdata['town']=profile.town
                userdata['state']=profile.state
                userdata['country']=profile.country
                data['user']=userdata
                print userdata
        template = loader.get_template('manager_users.html')
        context = {
        'data': data
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("login")


def adduser(request):
    if request.session.get('ismanagerloggedin', False):
        try:
            username=request.POST.get("username").strip()
            passwd=request.POST.get("password").strip()
            password=hashlib.sha256(passwd).hexdigest()
            firstname=request.POST.get("surname").strip()
            lastname=request.POST.get("lastname").strip()
            telephone=str(request.POST.get("telephone")).strip()
            email=request.POST.get("email").strip()
            skype=str(request.POST.get("skype")).strip()
            address1=str(request.POST.get("address1")).strip()
            address2=str(request.POST.get("address2")).strip()
            city=str(request.POST.get("city"))
            town=str(request.POST.get("town"))
            state=str(request.POST.get("state"))
            country=str(request.POST.get("country"))
            checkuser=User.objects.raw("SELECT * FROM api_user,api_profile where api_user.id=api_profile.uid AND (api_user.username='"+username+"' OR api_profile.email='"+email+"' OR api_profile.phone='"+telephone+"')")
            if len(list(checkuser))<=0:
                user=User.objects.create(username=username,password=password,createdate=timezone.now())
                uid=user.id
                profile=Profile.objects.create(uid=uid,email=email,phone=telephone,skype=skype,address1=address1,address2=address2,createdate=timezone.now())
        except Exception as ex:
            print ex
        return HttpResponseRedirect("../users")
    else:
        return HttpResponseRedirect("../login")

def updateuser(request):
    if request.session.get('ismanagerloggedin', False):
        try:
            uid=request.POST.get("id")
            firstname=request.POST.get("surname").strip()
            lastname=request.POST.get("lastname").strip()
            telephone=str(request.POST.get("telephone")).strip()
            email=request.POST.get("email").strip()
            skype=str(request.POST.get("skype")).strip()
            address1=str(request.POST.get("address1")).strip()
            address2=str(request.POST.get("address2")).strip()
            city=str(request.POST.get("city"))
            town=str(request.POST.get("town"))
            state=str(request.POST.get("state"))
            country=str(request.POST.get("country"))
            checkuser=User.objects.raw("SELECT * FROM api_user,api_profile where api_user.id=api_profile.uid AND (api_user.id='"+uid+"' OR api_profile.email='"+email+"' OR api_profile.phone='"+telephone+"')")
            if len(list(checkuser))>0:
                profile=Profile.objects.get(uid=uid)
                print profile
                profile.email=email
                profile.firstname=firstname
                profile.lastname=lastname
                profile.phone=telephone
                profile.skype=skype
                profile.address1=address1
                profile.address2=address2
                #profile.city=city
                #profile.town=town
                #profile.state=state
                #profile.country=country
                profile.save()
        except Exception as ex:
            print ex
        return HttpResponseRedirect("../users")
    else:
        return HttpResponseRedirect("../login")


def deleteuser(request,uid):
    if request.session.get('ismanagerloggedin', False):
        try:
            user=User.objects.get(id=uid)
            profile=Profile.objects.get(uid=uid)
            user.delete()
            profile.delete()
        except Exception as ex:
            print ex
        return HttpResponseRedirect("../../users")
    else:
        return HttpResponseRedirect("../../login")

def changestatus(request,uid):
    if request.session.get('ismanagerloggedin', False):
        try:
            user=User.objects.get(id=uid)
            if user.status==0:
                user.status=1
            else:
                user.status=0
            user.save()
        except Exception as ex:
            print ex
        return HttpResponseRedirect("../../users")
    else:
        return HttpResponseRedirect("../../login")

def listusers(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        offset=request.GET['offset']
        limit=request.GET['limit']
        pager="LIMIT "+offset+","+limit
        users=User.objects.raw("SELECT  api_user.id as id,firstname,lastname,email,phone,username,status,api_user.createdate as createdate from api_user,api_profile WHERE api_user.id=api_profile.uid "+pager)
        data={}
        data['total']= User.objects.count()
        data['rows']=usersToJson(users)
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")

def fetchuser(request,uid):
    if request.session.get('ismanagerloggedin', False):
        data={}
        users=User.objects.raw("SELECT  api_user.id as id,firstname,lastname,email,phone,username,status,api_user.createdate as createdate from api_user,api_profile WHERE api_user.id=api_profile.uid AND api_user.id="+uid)
        data={}
        data['total']= User.objects.count()
        data['rows']=usersToJson(users)
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")


#subscribers
def subscription(request):
    template = loader.get_template('manager_subscription.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def createsubscription(request):
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


def deletesubscription(request):
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

def listsubscription(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        offset=request.GET['offset']
        limit=request.GET['limit']
        pager="LIMIT "+offset+","+limit
        users=User.objects.raw("SELECT  api_user.id as id,firstname,lastname,email,telephone,username,isphoneverified,isemailverified,status,api_user.createdate as createdate from api_user,api_profile WHERE api_user.id=api_profile.uid "+pager)
        data={}
        data['total']= User.objects.count()
        data['rows']=usersToJson(users)
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")

def updatesubscription(request):
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