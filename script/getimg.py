# -*- coding:utf-8 -*-
import re
import requests
from PIL import Image

# if __name__ == '__main__':
#     word = '酒席'
#     url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
#     result = requests.get(url)
#     dowmloadPic(result.text)

import urllib.request
import re


# 浏览器伪装
def pretends():
    headers = ("Uesr-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)


# 爬取函数，参数为:搜索关键词， 页数
def crawl(keyword, maxpics):
    count = 1
    k = 0
    enouth = False
    while not enouth:
        try:
            key = urllib.request.quote(keyword)
            url = "https://image.baidu.com/search/flip?tn=baiduimage&word=" + key + "&pn=" + str(k * 20)
            k += 1
            data = urllib.request.urlopen(url).read().decode('utf-8')
            print(len(data))
            pat = '"objURL":"(.*?)",'
            rst = re.compile(pat).findall(data)
            cnt = 0
            for i in range(0, len(rst)):
                # 添加异常处理
                try:
                    # 获取图片扩展名
                    pat1 = '\.[^.\\/:*?"<>|\r\n]+$'
                    rst1 = re.compile(pat1).findall(rst[i])
                    # 下载图片到本地
                    urllib.request.urlretrieve(rst[i], "images/" + str(count) + rst1[0])
                    img = Image.open("images/" + str(count) + rst1[0])
                    copy = img.copy()
                    copy.thumbnail((1000, 583), Image.BICUBIC)
                    width, height = copy.size
                    n_im = Image.new("RGB", (1000, 583), "black")
                    n_im.paste(copy, (int((1000 - width) / 2), int((583 - height) / 2)))
                    n_im.save("cutimgs/" + str(count) + rst1[0])
                    count += 1
                    if count > maxpics:
                        enouth = True
                        break
                    print('正在下载：%s' % count)
                except Exception as err:
                    print(err)
        except Exception as err:
            print("出现异常:" + str(err))


def main():
    pretends()
    crawl("一桌美食", 1000)


if __name__ == '__main__':
    main()
