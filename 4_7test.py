import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import re
def down_img(url):
    print('当前处理的页面是',url)
    resp=requests.get(url)
    resp.encoding='gbk'
    html=etree.HTML(resp.text)
    # 判断链接是否含有_
    if_url=url.find('_')
    if if_url==-1:
        div=html.xpath('//*[@id="main"]/div[4]/ul/li/a')
    else:
        div = html.xpath('//*[@id="main"]/div[3]/ul/li/a')
    for i in div:
        res_url=i.xpath('./@href')[0]
        # 拼接链接
        s=url.split('/i')[0]+res_url
        # 进入子链接
        re_spurl=requests.get(s)
        re_spurl.encoding = 'gbk'
        html_a=etree.HTML(re_spurl.text)
        div_a=html_a.xpath('//*[@id="main"]/div[3]/div/p/a')
        for j in div_a:
            url_img=j.xpath('./img/@src')[0]
            str(url_img)
            #下载图片
            down_img_url=requests.get(str(url_img))
            img_name = str(url_img).split('/')[-1]
            with open('img/' + img_name, mode='wb') as f:
                f.write(down_img_url.content)  # 写入文件
                print('下载成功', img_name)
if __name__=='__main__':
    t=ThreadPoolExecutor(30) #线程数
    for i in range(1,1208): #http://www.netbian.com/index.htm
        if i==1:
            t.submit(down_img,f'http://www.netbian.com/index.htm')
        else:
            t.submit(down_img,f'http://www.netbian.com/index_{i}.htm')

