## install

$ pip install selenium


## Selenium IDE


## Selenium with Python

Selenium with Python: [http://selenium-python.readthedocs.org/](http://selenium-python.readthedocs.org/)

Selenium Browser automation framework: [https://code.google.com/p/selenium/wiki/ChromeDriver](https://code.google.com/p/selenium/wiki/ChromeDriver)

ChromeDriver - WebDriver for Chrome: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)


## ChromeDriver

[http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html)


## os、sys、platform 三个模块

另外稍微区分一下 os、sys、platform 三个模块

- os 提供操作系统的接口，常用的有文件系统相关和进程相关
例如：
> os.path.walk (遍历目录)
> os.getpid (获取进程id)


- sys 提供 python 解释器系统的通用配置和函数，影响着解释器的行为
注意这里的系统不是操作系统，而是 python 解释器这个“系统”
例如：
> sys.version (python版本而非os版本)
> sys.path (模块搜索路径，不是os的环境变量)
> sys.getrecursionlimit (最大嵌套调用层数)
> sys.getrefcount (获取对象的引用计数)

- platform 提供平台相关的信息
例如：
> platform.architecture (操作系统和位数)
> platform.processor (处理器版本)

```
>>> import platform
>>> platform.machine()
AMD64
```


sys.platform

| 平台 | 值 |
| --- | --- |
| Linux (2.x and 3.x) | linux2 |
| Windows | win32 |
| Windows/Cygwin | cygwin |
| Mac OS X | darwin |
| OS/2 | os2 |
| OS/2 EMX | os2emx |
| RiscOS | riscos |
| AtheOS | atheos |


- Ubuntu 32bit
```
>>> import platform
>>> platform.machine()
'i686'
>>> platform.system()
'Linux'
>>> import sys
>>> sys.platform
'linux2'
```


- Ubuntu 64bit
```
>>> import platform
>>> platform.machine()
'x86_64'
>>> platform.system()
'Linux'
>>> import sys
>>> sys.platform
'linux2'
```


- Mac 64bit
```
>>> import platform
>>> platform.machine()
'x86_64'
>>> platform.system()
'Darwin'
>>> import sys
>>> sys.platform
'darwin'
```

- Win 32bit
```
>>> import platform
>>> platform.machine()
'x86'
>>> platform.system()
'Windows'
>>> import sys
>>> sys.platform
'win32'
```

- Win 64bit
```
>>> import platform
>>> platform.machine()
'AMD64'
>>> platform.system()
'Windows'
>>> import sys
>>> sys.platform
'win32'
```


## Using Selenium with remote WebDriver

如果仅仅是本地测试/调试，可以使用本地驱动看到浏览器操作界面；

生产环境往往不需要也没有桌面环境，这时就需要远程驱动配合Xvfb（虚拟图形服务）。

http://seleniumhq.github.io/selenium/docs/api/py/#selenium-server-optional

http://selenium-python.readthedocs.io/getting-started.html#using-selenium-with-remote-webdriver

下载
```
wget -c http://selenium-release.storage.googleapis.com/3.0/selenium-server-standalone-3.0.0.jar
```

Mac 环境依赖
```
brew install chromedriver
brew doctor
```

启动服务
```
java -jar selenium-server-standalone-3.0.0.jar
```

调用服务
```
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME
)
```


## 项目要点

解析失败，页面链接和整个页面文件保存下来。



## 51job简历文本解析过程

1年工作经验 | 男 |  24岁（1991年9月18日）
2年工作经验 | 男 |  24岁（1992年1月2日） |  未婚
1年工作经验 | 女 |  23岁（1992年6月1日） |  未婚 |  168cm |  中共党员
2年工作经验 | 男 |  25岁（1991年1月31日） |  已婚 |  183cm |  群众


> 填表单，登陆
> 进入简历收件箱
> 获取简历列表信息，自动翻页
> 获取简历详情页面

