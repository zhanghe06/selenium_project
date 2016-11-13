## Xvfb

Xvfb - virtual framebuffer X server for X Version 11

Xvfb is an X server that can run on machines with no display hardware and no physical input devices.
It emulates a dumb framebuffer using virtual memory.

```
$ sudo apt-get install xvfb
```

## PyVirtualDisplay

PyVirtualDisplay is a python wrapper for Xvfb, Xephyr and Xvnc

```
$ pip install pyvirtualdisplay
```

[PyVirtualDisplay Doc](http://pyvirtualdisplay.readthedocs.io/en/latest/)

[PyVirtualDisplay GitHub](https://github.com/ponty/pyvirtualdisplay)


## xephyr

display = Display(visible=True)

当设置 visible=True 时, 需要安装 xephyr
```
$ sudo apt-get install xserver-xephyr
```

## CutyCapt

CutyCapt is a small cross-platform command-line utility to capture WebKit's rendering of a web page into a variety of vector and bitmap formats, including SVG, PDF, PS, PNG, JPEG, TIFF, GIF, and BMP. See IECapt for a similar tool based on Internet Explorer.

[http://cutycapt.sourceforge.net/](http://cutycapt.sourceforge.net/)

```
$ sudo apt-get install cutycapt
```

通过 cutycapt 配合 xvfb 截取网页保存为本地图片

```
$ cutycapt --url=http://www.baidu.com --out=localfile.png
```

```
$ xvfb-run -s "-screen 0 1024x768x24" cutycapt --url=http://www.baidu.com --out=localfile.png --body-string=utf-8
```