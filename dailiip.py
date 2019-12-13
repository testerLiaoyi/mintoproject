
def get_random_header():
    headers={'User-Agent':random.choice(user_agent.list),'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",'Accept-Encoding':'gzip'}
    return headers

def   scraw_proxies(page_num,scraw_url="http://www.xicidaili.com/nt/"):
    scraw_ip=list()
    available_ip=list()
    for page in range(1,page_num):
        print("抓取第%d页代理IP" %page)
        url=scraw_url+str(page)
        r=requests.get(url,headers=get_random_header())
        r.encoding='utf-8'
        pattern = re.compile('<td class="country">.*?alt="Cn" />.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.S)
        scraw_ip= re.findall(pattern, r.text)
        for ip in scraw_ip:
            if(test_ip(ip)==True):
                print('%s:%s通过测试，添加进可用代理列表' %(ip[0],ip[1]))
                available_ip.append(ip)
            else:
                pass
        print("代理爬虫暂停10s")
        time.sleep(10)
        print("爬虫重启")
    print('抓取结束')
    return available_ip

if __name__=="__main__":
    available_ip=scraw_proxies(3)
def test_ip(ip,test_url='http://2017.ip138.com/ic.asp',time_out):
    proxies={'http': ip[0]+':'+ip[1]}
    try_ip=ip[0]
    #print(try_ip)
    try:
        r=requests.get(test_url,headers=get_random_header(),proxies=proxies,timeout=time_out)
        if r.status_code==200:
            r.encoding='gbk'
            result=re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',r.text)
            result=result.group()
            if result[:9]==try_ip[:9]:
                print(r.text)
                print('测试通过')
                return True
            else:
                print('%s:%s 携带代理失败,使用了本地IP' %(ip[0],ip[1]))
                return False
        else:
            print('%s:%s 请求码不是200' %(ip[0],ip[1]))
            return False
    except:
        print('%s:%s 请求过程错误' %(ip[0],ip[1]))
        return False
