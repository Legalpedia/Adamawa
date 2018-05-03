from imports import *


def documents(request):
    if request.session.get('ismanagerloggedin', False):
        if request.GET.get("action")!=None:
            action=request.GET.get("action")
            if action=="edit":
                id=request.GET.get("id")
                document=DocumentDownloads.objects.get(id=id)
                docdata={}
                docdata['id']=document.id
                docdata['name']=document.name
                docdata['description']=document.description
                docdata['price']=document.price
                docdata['contenturl']=document.contenturl
                docdata['previewurl']=document.previewurl
                docdata['image']=document.image
                data['documents']=docdata
                print docdata
        template = loader.get_template('manager_documents.html')
        context = {
        'data': data
        }
        return HttpResponse(template.render(context, request))
    else:
        request.session['isloggedin'] = False
        return HttpResponseRedirect("/manager/login")

def document_upload(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        name = request.POST.get("name")
        description = request.POST.get("description").strip()
        price = request.POST.get("price").strip()
        image = request.FILES.get('image')
        content = request.FILES.get('document')
        checkdocument = DocumentDownloads.objects.filter(name=name)
        if len(list(checkdocument)) <= 0:
            contenturl = handleContent(content)
            previewurl = handlePreview(content, contenturl)
            print previewurl
            print contenturl
            document = DocumentDownloads.objects.create(name=name,description=description,price=price,image=image,contenturl=contenturl,previewurl=previewurl,createdate=timezone.now())
            print document
            request.session['status'] = "ok"
            request.session['message'] = "successfully uploaded document"
        else:
            request.session['status']="failed"
            request.session['message']="document already exists"
        print request.session['status']
        return HttpResponseRedirect("/manager/documents")
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("/manager/login")


def listdocuments(request):
    if request.session.get('ismanagerloggedin', False):
        data={}
        offset=request.GET['offset']
        page=int(offset)/10
        documents = DocumentDownloads.objects.all()
        paginator = Paginator(documents, 10)
        try:
            document = paginator.page(page)
        except PageNotAnInteger:
            document = paginator.page(1)
        except EmptyPage:
            document = paginator.page(paginator.num_pages)
        productlist=documentsToJson(documents)
        data['total']= DocumentDownloads.objects.count()
        data['rows']=productlist
        return JsonResponse(data)
    else:
        request.session['ismanagerloggedin']=False
        return HttpResponseRedirect("login")


def updatedocuments(request):
    if request.session.get('ismanagerloggedin', False):
        try:
            docid = request.POST.get("docid")
            name=request.POST.get("name")
            description=request.POST.get("description").strip()
            price=request.POST.get("price").strip()
            image = request.FILES.get('image')
            content=request.FILES.get('content')
            print content.name
            checkdocument=DocumentDownloads.objects.filter(id=docid)
            if len(list(checkdocument))>0:
                image=""
                contenturl =handleContent(content)
                previewurl=handlePreview(content,contenturl)
                print previewurl
                print contenturl
                document=DocumentDownloads.objects.get(id=docid)
                print document
                document.name=name
                document.description=description
                document.price=price
                document.image=image
                document.contenturl=contenturl
                document.previewurl=previewurl
                document.save()
        except Exception as ex:
            print ex
        return HttpResponseRedirect("/manager/documents")
    else:
        return HttpResponseRedirect("/manager/login")


def handleImage(content):
   newfilename = str(uuid.uuid4()) + ".pdf"
   writeFile(newfilename,content)
   return newfilename


def handleContent(content):
   newfilename = str(uuid.uuid4()) + ".pdf"
   writeFile(newfilename,content)
   return newfilename

def handlePreview(content,filename):
   samplefile = str(uuid.uuid4()) + ".pdf"
   samplepath= "static/downloads/samples/"+samplefile
   path = "static/downloads/main/" + filename
   generateSample(samplepath,path)
   return samplefile


def writeFile(newfilename,content):
    path="static/downloads/main/"+newfilename
    fd = open(path, 'wb+')
    for chunk in content.chunks():
        fd.write(chunk)
	fd.close()
    return path

def generateSample(samplepath,path):
    originalpdf = PdfReader(path)
    output = PdfWriter()
    totalpages=len(originalpdf.pages)
    if totalpages>5:
        for i in range(1):
            page= originalpdf.pages[i]
            if page.Contents is not None:
                output.addpage(page)
        output.write(samplepath)

