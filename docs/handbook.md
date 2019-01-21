```
import requests
from bs4 import BeautifulSoup             # 从bs4这个库中导入BeautifulSoup

link = "http://www.santostang.com/"       # 网址
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Chrome/71.0.3578.98'}

resp = requests.get(link, headers = headers)    # 请求内容

soup = BeautifulSoup(resp.text, "lxml")   # 使用BeautifulSoup解析这段代码

title = soup.find("h1", class_ = "post-title").a#.text.strip()

soup.find("h1", class_ = "post-title")

# find 找到 class 是 post-title的 h1标签内容
<h1 class="post-title"><a href="http://www.santostang.com/2018/07/15/4-3-%e9%80%9a%e8%bf%87selenium-%e6%a8%a1%e6%8b%9f%e6%b5%8f%e8%a7%88%e5%99%a8%e6%8a%93%e5%8f%96/">4.3 通过selenium 模拟浏览器抓取</a></h1>

soup.find("h1", class_ = "post-title").a

# 找到h1标签内的a标签
<a href="http://www.santostang.com/2018/07/15/4-3-%e9%80%9a%e8%bf%87selenium-%e6%a8%a1%e6%8b%9f%e6%b5%8f%e8%a7%88%e5%99%a8%e6%8a%93%e5%8f%96/">4.3 通过selenium 模拟浏览器抓取</a>

soup.find("h1", class_ = "post-title").a.text

# 找到h1标签内的a标签内的内容text
4.3 通过selenium 模拟浏览器抓取

# 去除字符串头尾的空格
soup.find("h1", class_ = "post-title").a.text.strip()
```

strip() 方法用于移除字符串头尾指定的字符(默认为空格或换行符)或字符序列，返回处理后的新字符串。

```
str.strip([chars])      # chars -- 移除字符串头尾指定的字符序列
```