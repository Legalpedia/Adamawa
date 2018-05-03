from imports import *


#create account
def createaccount(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        name=request.POST['name']
        description=request.POST['description']
        account=Account.objects.create(name=name,description=description)
        return HttpResponseRedirect("../account")
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")



#update account
def updateaccount(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        id=request.POST["id"]
        uid=request.POST["uid"]
        accttype=request.POST["accttype"]
        lastrenewaldate=request.POST["lastrenewaldate"]
        nextrenewaldate=request.POST["nextrenewaldate"]
        createdate=request.POST["createdate"]
        account=Account.objects.update(uid=uid,accttype=accttype,lastrenewaldate=lastrenewaldate,nextrenewaldate=nextrenewaldate,createdate=createdate)
        data={}
        data['total']= Account.objects.count()
        data['rows']=accountToJson(account)
        return JsonResponse(data)
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")

#list account
def listaccount(request):
    if request.session.get('isloggedin', False):
        if request.method == "GET":
            response=verifySignature(request)
            if response['status']=="failed":
                return JsonResponse(response)
            try:
                account=Account.objects.all()
                listdata=getAccountDict(account)
                data={}
                data['account']=listdata
                data['status']="ok"
                data['message']=MESSAGE.ACCOUNT_SUCCESS
            except Exception as ex:
                data={}
                data['status']="failed"
                data['message']=MESSAGE.ACCOUNT_FAIL
            return JsonResponse(data)
        else:
            data={}
            data['status']="failed"
            data['message']=MESSAGE.INVALID_REQUEST_GET
            return JsonResponse(data)
    else:
        data={}
        data['status']="failed"
        data['message']=MESSAGE.INVALID_SESSION
        return JsonResponse(data)

#delete account
def deleteaccount(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        id=request.GET.get('id','')
        account=Account.objects.get(id=id)
        account.delete()
        return HttpResponseRedirect("../account")
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")


#create accounttype
def createaccounttype(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        name=request.POST['name']
        description=request.POST['description']
        accounttype=AccountType.objects.create(name=name,description=description)
        return HttpResponseRedirect("../accounttype")
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")



#update accounttype
def updateaccounttype(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        id=request.POST["id"]
        validity=request.POST["validity"]
        name=request.POST["name"]
        accounttype=AccountType.objects.update(validity=validity,name=name)
        data={}
        data['total']= AccountType.objects.count()
        data['rows']=accounttypeToJson(accounttype)
        return JsonResponse(data)
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")

#list accounttype
def listaccounttype(request):
    if request.session.get('ismanagerloggedin', False):
        if request.method == "GET":
            response=verifySignature(request)
            if response['status']=="failed":
                return JsonResponse(response)
            try:
                accounttype=AccountType.objects.all()
                listdata=getAccounttypeDict(accounttype)
                data={}
                data['accounttype']=listdata
                data['status']="ok"
                data['message']=MESSAGE.ACCOUNTTYPE_SUCCESS
            except Exception as ex:
                data={}
                data['status']="failed"
                data['message']=MESSAGE.ACCOUNTTYPE_FAIL
            return JsonResponse(data)
        else:
            data={}
            data['status']="failed"
            data['message']=MESSAGE.INVALID_REQUEST_GET
            return JsonResponse(data)
    else:
        data={}
        data['status']="failed"
        data['message']=MESSAGE.INVALID_SESSION
        return JsonResponse(data)

#delete accounttype
def deleteaccounttype(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        id=request.GET.get('id','')
        accounttype=AccountType.objects.get(id=id)
        accounttype.delete()
        return HttpResponseRedirect("../accounttype")
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")