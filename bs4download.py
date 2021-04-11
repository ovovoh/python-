# 1.拿主页面源代码
# 2.解析源代码拿到链接
import requests
for i in range(1,1209):
    if i==1:
        url = 'http://www.netbian.com'
        resp = requests.get(url)
        resp.encoding = "utf-8"  # 处理乱码
        resp_text = resp.text
        obj = BeautifulSoup(resp_text, "html.parser")
        div = obj.find('div', class_="list").find_all("a")
        # print(div)
        url_list=[] #储存url链接
        for i in div:
            src_download=url+i.get("href")
            url_list.append(src_download)
        # 删除重复错误的的链接
        url_list.remove("http://www.netbian.comhttps://pic.netbian.com/")
        url_list.remove("http://www.netbian.comhttps://pic.netbian.com/")
        
        print(url_list)
        
        for i in url_list:
            # print(i)
            get_download_resp=requests.get(i)
            get_download_resp.encoding = "utf-8"  # 处理乱码
            get_download_resp_text=get_download_resp.text
            # print(get_download_resp_text)
            obj1=BeautifulSoup(get_download_resp_text,"html.parser")
            find_div=obj1.find('div',class_='endpage')
            find_a=find_div.find('div',class_='pic').find_all('img')
            for i in find_a:
                src=i.get("src")
                img_resp=requests.get(src)
                img_name=src.split("/")[-1] #命名图片名字
        
                with open("img/"+img_name,mode='wb') as f:
                    f.write(img_resp.content) #拿到字节并写进文件
                print('download success',img_name)
        f.close()
        pass
    else:

        url = f'http://www.netbian.com/index_{i}.htm'
        resp = requests.get(url)
        resp.encoding = "gbk"  # 处理乱码
        resp_text = resp.text
        # print(resp_text)

        obj = BeautifulSoup(resp_text, "html.parser")
        div = obj.find('div', class_="list").find_all("a")
        # print(div)

        url_list = []  # 储存url链接
        for i in div:
            src_download = 'http://www.netbian.com'+ i.get("href")
            url_list.append(src_download)

        # 删除重复错误的的链接

        url_list.remove("http://www.netbian.comhttps://pic.netbian.com/")
        url_list.remove("http://www.netbian.comhttps://pic.netbian.com/")

        print(url_list)


        for i in url_list:
            # print(i)
            get_download_resp = requests.get(i)
            get_download_resp.encoding = "utf-8"  # 处理乱码
            get_download_resp_text = get_download_resp.text
            # print(get_download_resp_text)
            obj1 = BeautifulSoup(get_download_resp_text, "html.parser")
            find_div = obj1.find('div', class_='endpage')
            find_a = find_div.find('div', class_='pic').find_all('img')
            for i in find_a:
                src = i.get("src")
                img_resp = requests.get(src)
                img_name = src.split("/")[-1]  # 命名图片名字

                with open("img/" + img_name, mode='wb') as f:
                    f.write(img_resp.content)  # 拿到字节并写进文件
                print('download success', img_name)
        f.close()


