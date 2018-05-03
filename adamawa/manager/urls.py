from django.conf.urls import url
from . import views



app_name="manager"
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'login', views.login, name='login'),
url(r'logout', views.logout, name='logout'),
url(r'auth', views.auth, name='auth'),
url(r'chapters', views.chapters, name='chapters'),
url(r'document_upload', views.document_upload, name='document_upload'),
url(r'documents/list', views.listdocuments, name='listdocuments'),
url(r'documents/update', views.updatedocuments, name='updatedocuments'),
url(r'documents', views.documents, name='documents'),
url(r'uploadlaws', views.uploadlaws, name='uploadlaws'),
url(r'laws_upload', views.laws_main, name='laws_main'),
url(r'laws/list', views.listlaws, name='listlaws'),
url(r'laws/section/(?P<id>\d+)/', views.listsections, name='listsections'),
url(r'laws', views.laws, name='laws'),
url(r'createlaw', views.createlaw, name='createlaw'),
url(r'createsection', views.createsection, name='creatsections'),
url(r'sms', views.sms, name='sms'),

url(r'email', views.email, name='email'),

url(r'users/add', views.adduser, name='adduser'),
url(r'users/delete/(?P<uid>\d+)', views.deleteuser, name='deleteuser'),
url(r'users/status/(?P<uid>\d+)', views.changestatus, name='changestatus'),
url(r'users/update', views.updateuser, name='updateuser'),
url(r'users/fetch', views.fetchuser, name='fetchuser'),
url(r'users/list', views.listusers, name='listusers'),
url(r'users', views.users, name='users'),


url(r'newupdate/generate', views.newupdate, name='newupdate'),
url(r'newupdate/create', views.editor, name='editor'),
url(r'newupdate/delete', views.editor, name='editor'),
url(r'newupdate/list', views.editor, name='editor'),
url(r'newupdate', views.newupdate, name='newupdate'),


url(r'package/create', views.createpackage, name='createpackage'),
url(r'package/delete', views.deletepackage, name='deletepackage'),
url(r'package/list', views.listpackage, name='listpackage'),
url(r'package/update', views.updatepackage, name='updatepackage'),
url(r'package', views.package, name='package'),



url(r'license/create', views.generatelicenses, name='generatelicenses'),
url(r'license/delete', views.deletelicense, name='deletelicense'),
url(r'license/list', views.listlicense, name='listlicense'),
url(r'license/update', views.updatelicense, name='updatelicense'),
url(r'license', views.license, name='license'),


url(r'resource/create', views.createresource, name='createresource'),
url(r'resource/list', views.listresource, name='listresource'),
url(r'resource/update', views.updateresource, name='updateresource'),
url(r'resource/delete', views.deleteresource, name='deleteresource'),
url(r'resource', views.resource, name='resource'),


url(r'subscription/create', views.createsubscription, name='createsubscription'),
url(r'subscription/list', views.listsubscription, name='listsubscription'),
url(r'subscription/update', views.updatesubscription, name='updatesubscription'),
url(r'subscription/delete', views.deletesubscription, name='deletesubscription'),
url(r'subscription', views.subscription, name='subscription'),

url(r'transactions/list', views.listtransactions, name='listtransactions'),
#url(r'transactions/create', views.editor, name='editor'),
#url(r'transactions/update', views.editor, name='editor'),
#url(r'transactions/delete', views.editor, name='editor'),
url(r'transactions', views.transactions, name='transactions'),
url(r'sales/list', views.listsales, name='listsales'),
#url(r'transactions/create', views.editor, name='editor'),
#url(r'transactions/update', views.editor, name='editor'),
#url(r'transactions/delete', views.editor, name='editor'),
url(r'sales', views.sales, name='sales'),
#url(r'promo/create', views.editor, name='editor'),
#url(r'promo/update', views.editor, name='editor'),
#url(r'promo/delete', views.editor, name='editor'),
url(r'promo', views.promo, name='promo'),

]
