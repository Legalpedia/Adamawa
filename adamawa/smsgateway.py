import requests


class SMSGateway:
    def __init__(self,url,username,password):
        self.username=username
        self.password=password
        self.url=url
        self.client=requests.Session()

    def sendMessage(self,method,endpoint,params):
        if method=="POST":
            data={}
            for p in params:
                data[p]=params[p]
                    
            url=self.url+"/"+endpoint
            response=self.client.post(url,data=data)
            print response.text
        else:
            url=self.url+"/"+endpoint
            i=0
            for p in params:
                if i<=0:
                    url=url+"?"+p+"="+params[p]
                else:
                    url=url+"&"+p+"="+params[p]
                i=i+1
            response=self.client.get(url)
            print response.text
            

if __name__=="__main__":
    url="http://www.estoresms.com"
    username="biddyweb"
    password="googleboy234"
    s=SMSGateway(url,username,password)
    method="GET"
    endpoint="smsapi.php"
    params={}
    params['username']=username
    params['password']=password
    params['sender']="Legalpedia"
    params['recipient']="2348135357510"
    params['message']="Welcome to legalpedia online. Your validation token is: 234567"
    s.sendMessage(method,endpoint,params)
        
