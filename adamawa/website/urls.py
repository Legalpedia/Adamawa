from django.conf.urls import url
from . import views
app_name="portal"
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'cart/add', views.addToCart, name='addToCart'),
url(r'cart/remove', views.removeFromCart, name='removeFromCart'),
url(r'cart/list', views.subscriptions, name='subscriptions'),
url(r'cart', views.cart, name='cart'),
url(r'checkoutcomplete', views.downloadpaymentcompleted, name='downloadpaymentcompleted'),
url(r'checkout', views.checkout, name='checkout'),
url(r'contactus', views.contactus, name='subscriptions'),
url(r'downloads', views.downloads, name='downloads'),
url(r'subscriptions', views.subscriptions, name='subscriptions'),
url(r'accounts', views.accounts, name='accounts'),
url(r'login', views.login, name='login'),
url(r'register', views.register, name='register'),
url(r'dopaymentdownload', views.dopaymentdownload, name='dopaymentdownload'),

]
