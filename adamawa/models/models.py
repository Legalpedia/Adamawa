from __future__ import unicode_literals

from django.db import models




# Create your models here.
#table containing admin
class Admin(models.Model):
    db_table = 'admin'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    role = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    createdate = models.DateTimeField('date created')

#table containing adminrole
class AdminRole(models.Model):
    db_table = 'adminrole'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    createdate = models.DateTimeField('date created')

#table containing countries
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)



#table containing download users
class DownloadUsers(models.Model):
    db_table = 'transactions'
    id = models.AutoField(primary_key=True)
    otherref = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    cartid = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    town = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    createdate = models.DateTimeField('date created')


#table containing documentdownloads
class DocumentDownloads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    contenturl = models.TextField(default="")
    previewurl = models.TextField(default="")
    image = models.TextField(default="")
    createdate = models.DateTimeField('date created')


#table containing transaction information
class DownloadTransactions(models.Model):
    db_table = 'transactions'
    id = models.AutoField(primary_key=True)
    documentid = models.IntegerField(default=0)
    downloadattempts = models.IntegerField(default=0)
    uid = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=20,decimal_places=2)
    description = models.CharField(max_length=1000)
    otherref = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    tax = models.DecimalField(max_digits=20,decimal_places=2)
    commission = models.DecimalField(max_digits=20,decimal_places=2)
    voucher_code = models.CharField(max_length=20)
    status = models.IntegerField(default=0)
    createdate = models.DateTimeField('date created')

#table containing documentdownloaditems
class DocumentItems(models.Model):
    id = models.AutoField(primary_key=True)
    tid = models.IntegerField(default=0)
    paymenttref = models.CharField(max_length=1000)
    name = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    contenturl = models.TextField(default="")
    previewurl = models.TextField(default="")
    image = models.TextField(default="")
    createdate = models.DateTimeField('date created')


#table containing transaction information
class Transactions(models.Model):
    db_table = 'transactions'
    id = models.AutoField(primary_key=True)
    packageinfo = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    uid = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=20,decimal_places=2)
    description = models.CharField(max_length=1000)
    otherref = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    tax = models.DecimalField(max_digits=20,decimal_places=2)
    commission = models.DecimalField(max_digits=20,decimal_places=2)
    voucher_code = models.CharField(max_length=20)
    status = models.IntegerField(default=0)
    createdate = models.DateTimeField('date created')

#table with user profile information
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(default=0)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
    skype = models.CharField(max_length=200)
    facetime = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.IntegerField(default=0)
    city_other = models.CharField(max_length=200)
    state = models.IntegerField(default=0)
    state_other = models.CharField(max_length=200)
    town = models.IntegerField(default=0)
    town_other = models.CharField(max_length=200)
    country = models.IntegerField(default=0)
    createdate = models.DateTimeField('date created')


#table with user login details
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    secret = models.CharField(max_length=500)
    status = models.IntegerField(default=0)
    is2faverified = models.IntegerField(default=0)
    isemailverified = models.IntegerField(default=0)
    role = models.IntegerField(default=0)
    createdate = models.DateTimeField('date created')

#table for user roles
#1= normal user
#2= normal admin user
#3= super admin user
class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


#table for user group
#A group a user can be subscribed to
class UserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


#table for user group
#A group a user can be subscribed to
class UserGroupList(models.Model):
    id = models.AutoField(primary_key=True)
    groupid = models.IntegerField(default=0)
    uid =   models.IntegerField(default=0)

#table containing user access
#user access
class UserAccess(models.Model):
    id = models.AutoField(primary_key=True)
    packageid = models.IntegerField(default=0)
    uid=models.IntegerField(default=0)


#table containing access types web,android,ios
class UserValidity(models.Model):
    id = models.AutoField(primary_key=True)
    uid=models.IntegerField(default=0)
    lastrenewdate = models.DateTimeField("")
    nextrenewdate = models.DateTimeField("")

#table containing subject matters
class UserAccessList(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(default=0)
    accesstype = models.IntegerField(default=0)

def documentsToJson(documents):
    documentlist=[]
    for s in documents:
        data={}
        data['id']=s.id
        data['name']=s.name
        data['price']=s.price
        data['description']=s.description
        data['previewurl']=s.previewurl
        documentlist.append(data)
    return documentlist

def documentsToJsonMobile(documents):
    documentlist=[]
    for s in documents:
        data={}
        data['id']=s.id
        data['name']=s.name
        data['price']=s.price
        data['description']=s.description
        data['previewurl']=settings.siteurl+"/static/img/book.png"
        documentlist.append(data)
    return documentlist


def countryToJson(country):
    countrylist=[]
    for s in country:
        data={}
        data['id']=s.id
        data['name']=s.name
        countrylist.append(data)
    return countrylist


def cartToJson(cart):
    cartlist=[]
    cartdata={}
    cartdata['total']=cart.total
    cartdata['count'] = cart.count
    for product in cart.products:
        data={}
        data['id']=product.id
        data['name']=product.name
        data['price']=product.price
        data['description']=product.description
        data['previewurl']=product.previewurl
        cartlist.append(data)
    cartdata['data'] = cartlist
    return cartdata