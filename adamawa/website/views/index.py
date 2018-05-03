from imports import *


def index(request):
    page = request.GET.get('page', 1)
    documents = DocumentDownloads.objects.all()
    paginator = Paginator(documents, 20)
    try:
        document = paginator.page(page)
    except PageNotAnInteger:
        document = paginator.page(1)
    except EmptyPage:
        document = paginator.page(paginator.num_pages)
    data['productgrid'] = document
    template = loader.get_template('website_index.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def downloads(request):
    template = loader.get_template('website_downloads.html')
    page = request.GET.get('page', 1)
    documents=DocumentDownloads.objects.order_by("name").all()
    paginator = Paginator(documents, 20)
    try:
        document = paginator.page(page)
    except PageNotAnInteger:
        document = paginator.page(1)
    except EmptyPage:
        document = paginator.page(paginator.num_pages)
    #productlist=documentsToJson(documents)
    data['products']=document
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def subscriptions(request):
    template = loader.get_template('website_subscriptions.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def login(request):

    return HttpResponseRedirect("/accounts")


def register(request):
    return HttpResponseRedirect("/accounts")

def accounts(request):
    template = loader.get_template('website_account.html')
    country = Country.objects.all()
    countrylist = countryToJson(country)
    data['country'] = countrylist
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def contactus(request):
    template = loader.get_template('website_contactus.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def checkout(request):
    template = loader.get_template('website_checkout.html')
    country=Country.objects.all()
    countrylist=countryToJson(country)
    data['country']=countrylist
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))


def checkoutcomplete(request):
    template = loader.get_template('api_checkoutcomplete.html')
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))

def addToCart(request):
    cart = Cart(request.session)
    product = DocumentDownloads.objects.get(id=request.GET.get('pid'))
    cart.add(product, price=product.price)
    data={}
    data['status']="ok"
    data['message']="added"
    data['cart'] = cartToJson(cart)
    return JsonResponse(data)

def removeFromCart(request):
    cart = Cart(request.session)
    product = DocumentDownloads.objects.get(id=request.GET.get('pid'))
    cart.remove(product)
    data={}
    data['status']="ok"
    data['message']="removed"
    data['cart'] = cartToJson(cart)
    return JsonResponse(data)


def cart(request):
    template = loader.get_template('website_cart.html')
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))


def dopaymentdownload(request):
    cart = Cart(request.session)
    country = request.POST.get("country")
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    address = request.POST.get("address")
    address1 = request.POST.get("address1")
    town = request.POST.get("town")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    username = request.POST.get("username")
    createaccount = request.POST.get("createaccount")
    print createaccount
    uid=0
    if createaccount=="on":
        #verify profile email exist
        profile=Profile.objects.filter(email=email)
        if len(list(profile))>0:
            request.session["status"]="failed"
            request.session["message"]="User with this email address exist already"
            return HttpResponseRedirect("/checkout")
        profile = Profile.objects.filter(phone=phone)
        if len(list(profile)) > 0:
            request.session["status"] = "failed"
            request.session["message"] = "User with this phone number exist already"
            return HttpResponseRedirect("/checkout")
        user = User.objects.filter(username=username)
        if len(list(profile)) > 0:
            request.session["status"] = "failed"
            request.session["message"] = "User with this username exist already"
            return HttpResponseRedirect("/checkout")
        user = User.objects.create(username=username,password=password,status=0,is2faverified=0,isemailverified=0,secret="",role=0,createdate=timezone.now())
        uid=user.id
        profile=Profile.objects.create(uid=uid,email=email,phone=phone,address=address,address1=address1,town=town,country=country)
    cartproducts=cart.products
    cartid=request.session.session_key
    transid = uuid.uuid4().hex.upper()
    #check if downloaduser with cart already exist
    try:
        userd=DownloadUsers.objects.filter(cartid=cartid)
        if userd.count()>0:
            notexist=False
        else:
            notexist = True
    except Exception as ex:
        print ex
        notexist=True
    if notexist:
        d= DownloadUsers.objects.create(cartid=cartid,reference=transid, firstname=firstname, lastname=lastname, email=email, address1=address,address2=address1, town=town, phone=phone, createdate=timezone.now())
    else:
        userd = DownloadUsers.objects.get(cartid=cartid)
        userd.firstname=firstname
        userd.lastname = lastname
        userd.email = email
        userd.address1 = address
        userd.address2 = address1
        userd.town = town
        userd.phone = phone
        userd.reference = transid
        userd.save()

    duration=0
    pid=0

    template = loader.get_template('website_payment.html')
    data['transid'] = transid
    data['payment_gateway']="paystack"#"kongapay"
    data['merchantid']="pk_test_294b393b858f07d85789bc1d0029a482568cf605" #"testmerchant"
    data['merchantname']="Adamawa State Government"
    data['phone']=phone
    data['callbackurl']="http://adamawa.mobilipia.com/completed"
    data['amount']=cart.total
    data['email']=email
    data['description']="Download of Adamawa State Laws"
    try:
        transaction=Transactions.objects.create(packageinfo=pid,duration=duration,uid=uid,tax=0.0,commission=0.0,voucher_code="",amount=data['amount'],reference=data['transid'],otherref="",description=data['description'],status=0,createdate=timezone.now())
        data['transactionid']=transaction.id
    except Exception as ex:
        print ex
    context = {
    'data': data
    }
    return HttpResponse(template.render(context, request))



def downloadpaymentcompleted(request):
    cart = Cart(request.session)
    transactionid=request.GET.get('transactionid',0)
    transaction=Transactions.objects.get(id=transactionid)
    if transaction.status==1:
        data['purchases'] = DocumentItems.objects.filter(tid=transactionid)
        data['message']="Your transaction was successful"
    elif transaction.status==0:
        url = "https://api.paystack.co/transaction/verify/"
        txnref = request.GET.get('reference', 'Not Available')
        fullurl = url + txnref
        secret_key = "sk_test_b9ffbfbaf3f29559d8945aed1b11b8b7d1db708a"
        headers = {"Authorization": "Bearer " + secret_key}
        res = requests.get(fullurl, headers=headers)
        response = json.loads(res.content)
        status = response['data']['status']
        amountgateway = response['data']['amount']
        reason = response['data']['gateway_response']
        data['txnref'] = txnref
        data['reference'] = transaction.reference
        amounttrans = transaction.amount * 100
        data['transdate'] = transaction.createdate
        data['amount'] = transaction.amount
        if amountgateway == amounttrans:
            products = cart.products
            transaction.status=1
            transaction.otherref=txnref
            transaction.save()
            data['message'] = "Your transaction was successful"
            purchases=generateContentLinks(cart.products)
            cartid = request.session.session_key
            userd = DownloadUsers.objects.get(cartid=cartid)
            userd.otherref=txnref
            userd.save()
            for p in purchases:
                print p
                DocumentItems.objects.create(name=p['name'], tid=transactionid, paymenttref=txnref, price=p['price'], contenturl=p['downloadlink'],
                          previewurl=p['previewurl'], image="", createdate=timezone.now())
            data['purchases']=DocumentItems.objects.filter(tid=transactionid)
            cart.clear()
            request.session.flush()
        else:
            data['message']="Amount does not match"


    else:
        data['message']="Unable to complete payment ("+reason+")"
    request.session['isloggedin']=False
    template = loader.get_template('website_checkoutcomplete.html')
    context = {
        'data': data
        }
    return HttpResponse(template.render(context, request))



def generateContentLinks(products):
    contentlinks=[]
    for p in products:
        data={}
        data['downloadlink']=settings.siteurl+"/static/downloads/main/"+p.contenturl
        data['name']=p.name
        data['price'] = p.price
        data['previewurl'] = settings.siteurl+"/static/downloads/samples/"+p.previewurl
        contentlinks.append(data)
    return contentlinks

