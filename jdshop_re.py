import requests
import  re

def getHtmlText():

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://search.jd.com/',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Origin': 'https://search.jd.com',
        'If-Modified-Since': 'Thu, 14 May 2020 11:33:47 GMT',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Pragma': 'no-cache',
    }

    params = (
        ('keyword', '思想本质'),
        ('enc', 'utf-8^'),
        ('suggest', '4.his.0.0^'),
        ('www', '^'),
        ('pvid', '60fd02742beb4eb78dc4f23c90b7fd31'),
    )
    try:
        response = requests.get('https://search.jd.com/Search', headers=headers, params=params)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        return  response.text
    except:
        print(response.raise_for_status())

def parsePage(flist,html):
    try:
        plt = re.findall(r'<em>\￥<\/em><i>[\d.]*<\/i>',html)
        nlt = re.findall(r'<i class=\"promo-words\" id=\"J_AD_[\d]*\">\S*<\/i>',html)
        blt = re.findall(r'<span class=\"p-bi-name\" onclick=.*>\s*<a title=\".*\" href=.* target=\".*\">.*<\/a>', html)
        for i in range(len(plt)):
            try:
                price = re.split('[><]',plt[i])
                bname = re.split('[><]',nlt[i])
                author = re.split('[><]',blt[i])
            except:
                pass
            flist.append([price[6],bname[2],author[4]])
    except:
        pass

def printGoodsList(flist):
    tflist = "{:4}\t{:<10}\t{:^0}"
    print(tflist.format("价格","简介","作者"))
    for g in flist:
        print(tflist.format(g[0],g[1],g[2]))
def main():
    flist = []
    html = getHtmlText()
    plist = parsePage(flist,html)
    printGoodsList(flist)

if __name__ == '__main__':
    main()
