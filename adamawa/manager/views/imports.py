# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader
from django.db.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from models.models import *
import time
import csv
from django.utils import timezone
from django.utils.encoding import *
import hashlib
from celery.result import AsyncResult
from celery.task.control import *
from celery import task, current_task,current_app
import os
import codecs
from celery import Celery
from django.conf import settings
from anyjson import serialize
import uuid
from os import listdir
from os.path import isfile, join
from django import template
from celery import task, current_task,subtask,chain
from celery.task.control import revoke
from celery.result import AsyncResult
from celery import group as celerygroup
from celery import current_app
from docx import Document
from pdfrw import PdfReader,PdfWriter
import untangle
import random, string
import uuid
import settings
import messages as MESSAGE
# Create your views here.
siteurl=settings.siteurl
data={"sitename":settings.sitename}


def verifySignature(request):
    if request.method == "GET":
        if "HTTP_X_AP_SIGNATURE" not in request.META:
            data['message']="invalid signature"
        if "HTTP_X_NL_API_VERSION" not in request.META:
            data['message']="unknown api version"
        if "HTTP_VERSION" not in request.META:
            data['message']="unknown app version"
        if "HTTP_X_NL_KEY" not in request.META:
            data['message']="invalid key"
        return JsonResponse(data)
    else:
        return JsonResponse(data)