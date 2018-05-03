from imports import *

def subscription(request):
    if request.session.get('ismanagerloggedin', False):
        data['username']=request.session.get("username")
        template = loader.get_template('manager_transactions.html')
        context = {
        'data': data
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("login")


def listsubscription(request):
    if request.session.get('ismanagerloggedin', False):
        print "List sections"
        data={}
        offset=request.GET['offset']
        limit=request.GET['limit']
        pager="LIMIT "+offset+","+limit
        transaction=Transactions.objects.raw("SELECT  a.id as id,b.username as username,amount,tax,description,commission,a.status,a.createdate as paymentdate from api_transactions a,api_user b WHERE a.uid=b.id  "+pager)
        data={}
        data['total']= len(list(Transactions.objects.raw("SELECT  a.id as id,b.username as username,amount,tax,description,commission,a.status,a.createdate as paymentdate from api_transactions a,api_user b WHERE a.uid=b.id")))
        data['rows']=transactionsToJson(transaction)
        return JsonResponse(data)
    else:
        request.session['isloggedin']=False
        return HttpResponseRedirect("login")