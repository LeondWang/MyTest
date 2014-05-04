import httplib, urllib2
from myutil import *
httplib.HTTPConnection.debuglevel = 1

url='http://172.30.138.174'
gbuf="freenet is freenet  what ever you do  you can always be good at such kind of things by learning more and more "

url2='http://translate.google.com/translate_t'
sensitive='hl=en&ie=UTF8&text=%B7%A8%C2%D6%B4%F3%B7%A8%BA%C3&langpair=zh-CN%7Cen'
def AddHeaders(request,clength):
    request.add_header('Accept', 'text/xml,text/html,image/gif,image/x-xbitmap,image/jpeg,image/pjpeg,application/x-shockwave-flash,application/vnd.ms-excel,application/vnd.ms-powerpoint,application/msword,*/*')
#    request.add_header('Referer','http://translate.google.com/translate_t')
    request.add_header('Accept-Language','zh-cn,zh;q=0.5')
#    request.add_header('Content-Type', 'text/plain')


    request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.2) Gecko/20061010 Firefox/2.0')
    request.add_header('Host','172.30.138.14')
#    request.add_header('Accept-Encoding','gzip,deflate')
#    request.add_header('Content-Encoding', 'gzip,deflate')
    if clength!=0:
        request.add_header('Content-Length', str(clength) )
    request.add_header('Keep-Alive','300')
    request.add_header('Connection','Keep-Alive')
#    request.add_header('Cache-Control','no-cache')
#    request.add_header('GoogleIP','good')


def SendRequestGzip(url,buf):
    zbuf=GzipBuf(buf)
    request =urllib2.Request(url,zbuf)
    opener = urllib2.build_opener()
    AddHeaders(request,len(zbuf))

    f = opener.open(request)

    db = f.read()
    print "length is :",len(db)
    if db[0]!='\002' or db[1]!='\377':
        print db
    else:
        print UnGzip(db)
    
    f.close()
    
def SendRequest(url,buf):
   
    request =urllib2.Request(url,buf)
    opener = urllib2.build_opener()
    AddHeaders(request,len(buf))
    f = opener.open(request)
    db = f.read()
    print "length is :",len(db)
    print db
    f.close()
def SendRequest1(url):

    request =urllib2.Request(url)
    opener = urllib2.build_opener()
    AddHeaders(request,0)
    f = opener.open(request)
    db = f.read()
    print "length is :",len(db)

    f1=open("save.htm","wb")
    f1.write(db)
    print db
    f.close()
#ln=os.path.getsize(filename)
#print UnGzip(GzipBuf(buf))
#UnGzip2File(GzipFile('in.txt'),'out.txt')
#SendRequest(url,buf)
#f=open("c:\proxyencoding.cc","r")




#SendRequest(url,"hello,world")
SendRequestGzip(url2,'hello')

xxxxx
