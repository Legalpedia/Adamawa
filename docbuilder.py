from docx import Document
from pdfrw import PdfReader,PdfWriter
import uuid
from datetime import *
import os
#directory="kwaradocuments"
directory="documents/PDFs"
savedirectory="static/downloads"
def getTitles():
    files=os.listdir(directory)
    for f in files:
       if ".docx" in f:
            path =os.getcwd()+"/"+directory+"/"+f
            d = Document(path)
            para = d.paragraphs
            print para[0].text
       if ".pdf" in f:
            print len(f.split("-"))
            if len(f.split("-"))>1:
                title = f.split("-")[1].strip().replace(".pdf","")
            else:
                title = f.strip().replace(".pdf","")
            newfilename=str(uuid.uuid4())+".pdf"
            path = os.getcwd() + "/"+directory+"/" + f
            savepath = os.getcwd()+"/"+savedirectory+"/main/"+newfilename
            samplefilename = str(uuid.uuid4()) + ".pdf"
            samplepath = os.getcwd() + "/" + savedirectory + "/samples/" + samplefilename
            moveToStatic(savepath,path)
            generateSample(samplepath,path)

            print samplefilename,newfilename,title
            writeToSQL(samplefilename,newfilename,title)

def writeToSQL(samplefilename,newfilename,title):
    data="INSERT INTO api_documentdownloads(name,description,price,imageurl,contenturl,previewurl,createdate) VALUES('%s','%s','%s','%s','%s','%s','%s');\n" % (title,title,"1000","",newfilename,samplefilename,datetime.now())
    with open("data.sql", "a+") as fout:
        fout.write(data)

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

def moveToStatic(savepath,path):
    with open(path, "r+") as fin:
        data = fin.read()
        with open(savepath, "w+") as fout:
            fout.write(data)


if __name__=="__main__":
    getTitles()