from imports import *
from lxml import etree
import re

def validateXML(xmlstr):
    print xmlstr

def writeFile(file):
    path="static/uploads/tmp/"+file.name
    fd = open(path, 'wb+')
    for chunk in file.chunks():
        fd.write(chunk)
	fd.close()
    #with open(path,"w+") as f:
    #    f.write(file.read())
    return path


def handleXMLDocument(path):
    document = Document(path)
    fullText = []
    for para in document.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)


def processLaw(document):
    try:
        title=document.chapter.title.cdata.encode("utf-8").strip()
    except Exception as ex:
        title=""
    try:
        cover=document.chapter.cover.cdata.encode("utf-8")
    except Exception as ex:
        cover=""
    try:
        lawnumber=document.chapter.lawnumber.cdata.encode("utf-8").strip()
    except Exception as ex:
        lawnumber=""
    try:
        lawdate=document.chapter.lawdate.cdata.encode("utf-8").strip()
        m = re.findall('Date of commencement: (.*?)]', lawdate, re.MULTILINE)
        lawdate=m[0]
    except Exception as ex:
        lawdate=""
    try:
        lawdesc=document.chapter.lawdescription.cdata.encode("utf-8").strip()
    except Exception as ex:
        lawdesc=""
    law=Laws.objects.create(title=title,cover=cover,number=lawnumber,date=lawdate,description=lawdesc,postdate=timezone.now(),updatedate=timezone.now())
    return law

def processSections(lawid,document):
    weightindex=0
    for section in document.chapter.sections.section:
            try:
                partschedule=section.partschedule.cdata.encode("utf-8").strip()
            except Exception as ex:
                partschedule=""
            try:
                title=section.heading.cdata.encode("utf-8").strip()
            except Exception as ex:
                title=""
            try:
                body=section.body.cdata.encode("utf-8").strip()
            except Exception as ex:
                body=""
            try:
                resource=Sections.objects.create(lawid=lawid,partschedule=partschedule,title=title,body=body,weightindex=weightindex,postdate=timezone.now(),updatedate=timezone.now())
            except Exception as ex:
                print ex
            weightindex= weightindex + 1

def processParts(lawid,document):
    for part in document.chapter.parts.part:
        parttitle=part.header.cdata.encode("utf-8").strip()
        weightindex = 0
        for section in part.sections.section:
                try:
                    partschedule=section.partschedule.cdata.encode("utf-8").strip()
                except Exception as ex:
                    partschedule=""
                try:
                    title=section.heading.cdata.encode("utf-8").strip()
                except Exception as ex:
                    title=""
                try:
                    body=section.body.cdata.encode("utf-8").strip()
                except Exception as ex:
                    body=""
                try:
                    section=Sections.objects.create(lawid=lawid,part=parttitle,partschedule=partschedule,title=title,body=body,weightindex=weightindex,postdate=timezone.now(),updatedate=timezone.now())
                except Exception as ex:
                    print ex
                weightindex = weightindex + 1

def processScheduleParts(lawid,document):
    for part in document.chapter.schedules.schedule.parts.part:
        parttitle=part.header.cdata.encode("utf-8").strip()
        weightindex = 0
        for section in part.sections.section:
                try:
                    partschedule=section.partschedule.cdata.encode("utf-8").strip()
                except Exception as ex:
                    partschedule=""
                try:
                    title=section.heading.cdata.encode("utf-8").strip()
                except Exception as ex:
                    title=""
                try:
                    body=section.body.cdata.encode("utf-8").strip()
                except Exception as ex:
                    body=""
                try:
                    section=Sections.objects.create(lawid=lawid,part=parttitle,partschedule=partschedule,title=title,body=body,weightindex=weightindex,postdate=timezone.now(),updatedate=timezone.now())
                except Exception as ex:
                    print ex
                weightindex = weightindex + 1

def processSchedules(lawid,document):
    for schedule in document.chapter.schedules.schedule:
        header=schedule.header.cdata.encode("utf-8").strip()
        lawnumber=schedule.lawnumber.cdata.encode("utf-8").strip()
        lawdate=schedule.lawdate.cdata.encode("utf-8").strip()
        try:
            if document.chapter.schedules.schedule.parts:
                processScheduleParts(lawid,document)
        except Exception as ex:
                #processScheduleParts(lawid,document)
                print ex


def updateDatabase(data):
    data="<?xml version='1.0' ?>\n"+data.encode("utf-8").strip()
    with open("data.xml","wb+") as f:
        f.write(data)
    document=untangle.parse(data)
    try:
        law=processLaw(document)
        lawid=law.id
        try:
            if document.chapter.parts:
                processParts(lawid,document)
        except Exception as ex:
            processSections(lawid,document)
        try:
            if document.chapter.schedules:
                processSchedules(lawid,document)
        except Exception as ex:
            print ex
    except Exception as ex:
       print ex

@task
def doUpload(result):
    files=result['files']
    for file in files:
        filename=file.name
        print filename
        try:
            path=writeFile(file)
            data=handleXMLDocument(path)
            updateDatabase(data)
        except Exception as ex:
            print ex
    pass