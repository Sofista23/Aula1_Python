from urllib import request
try:
    site=request.urlopen("http://pudim.com.br/")
except:
    print("O site PUDIM não está acessível no momento!")
else:
    print("Site acessível!")