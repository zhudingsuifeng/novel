# coding = utf-8

import requests
from bs4 import BeautifulSoup             # 从bs4这个库中导入BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Chrome/71.0.3578.98'}
resp = requests.get(link, headers = headers)

soup = BeautifulSoup(resp.text, "lxml")   # 使用BeautifulSoup解析这段代码
title = soup.find("h1", class_ = "post-title").a.text.strip()

print(title)