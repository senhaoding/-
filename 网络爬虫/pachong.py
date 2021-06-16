# 功能：实现网页的爬取
# 版本：v2.0
# 制作人：senhaoding

import urllib.request  #用于下载URL

from urllib.error import URLError,HTTPError,ContentTooShortError  #用于捕获下载URL时的错误异常

import re    #产生正则表达式来获取需要的url

def download(url,num_retrise=3,user_agent='wswp',charset='utf-8'):
#  下载url中的html代码
# （下载URL并检测异常）、（下载重试）、（修改代理，以防被网页拒绝访问）、（）
#  num_retrise为重试下载次数，user_agent为用户代理，charset为默认字符编码

    print('Downloading:',url)

    request=urllib.request.Request(url)  #使用Request（）来包装请求，再通过urlopen（）获取页面。

    request.add_header('User-agent',user_agent)
           #用于伪装成浏览器以防止被网页拒绝访问
    try:
        resp=urllib.request.urlopen(request,timeout=2) #timeout为访问超时时间，单位：s
        cs=resp.headers.get_content_charset() #获取字符编码头部
        if not cs:   #若没获得字符头部，则采用默认字符头部。
            cs=charset
        html=resp.read().decode(cs,errors="ignore")  #对读取的数据进行解码，其中decode（）为解码，而encode（）为编码。将errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。在这里改为ignore可避免某些解码错误

    except (URLError,HTTPError,ContentTooShortError)as e:
        print("Download error:",e.reason)
        html=None
        if num_retrise>0:
            if hasattr(e,'code')and 500<=e.code<600:  #由于404等错误短时间或者根本不可连接，故只需判断504之类的错误。
           #python中hasattr方法用于判断e这个类中有没有code这个属性。
           #recursively retry 5xx HTTP errors
               return download(url,num_retrise - 1) #对download（）迭代，以重试下载。
    return html


def get_allurl(url,times,path):    #利用正则表达式迭代爬取,并将html代码写入文件中。其中url为起始网址，times为爬取的层数。

    times=int(times)
    html_code=download(url)

    file = open(path+'\html1', 'w',encoding='utf-8')
    file.write(html_code)
    file.close()

    links=re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',html_code)  #利用正则表达式将下下来的url中匹配的字符串转换成数组

    links=tuple(set(links)) #set()函数用于去除重复


    for time in range(times-1):  #迭代下载
           print('times:{}'.format(time))
           url_html=download(str(links[time]))

           if url_html!=None:  #当发生下载url错误时跳过此url，否则写入文件中。
              file=open(path+'\html{}'.format(time+2),'w',encoding='utf-8')
              file.write(url_html)
              file.close()
           else:
               pass


    return





