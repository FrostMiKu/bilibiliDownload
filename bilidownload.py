#!/usr/bin/env python
# -*- coding: utf-8 -*-

u'输入AV号自动下载视频'

__author__ = 'FrostMiKu'

import json,urllib,os,sys,re

#GET请求
def http_get(av):
	url = 'https://api.kaaass.net/biliapi/video?id='+av
	html = urllib.urlopen(url)
	return html.read()
	
#正则匹配AV号输入格式是否正确
def is_av(av):
	x = re.match(r'[0-9]+',av)
	if x:
		return x.group(0)
	else:
		print(u'请输入纯数字AV号，例如AV233输入233\r')
		sys.exit(-1)

#回调函数
def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
		percent = 100
		print("%.2f%%" %percent)
		print('done!')
		return 0
    print("%.2f%%" %percent)

#下载视频
def download(url):
	#创建保存视频的目录
	if os.path.exists('Videos') == False:
		os.mkdir('Videos')
	#获取视频格式
	name1 = url[:url.index('?')]
	name2 = name1.replace(name1[:name1.rindex('.')],'')
	#以AV号命名视频
	name = 'AV' + av + name2
	#下载
	savepath = 'Videos/'+name
	urllib.urlretrieve(url,savepath,callbackfunc)

#起始位置
av = is_av(raw_input('请输入AV号，仅数字: '))
#解析json获取视频链接
js = http_get(av)
jsl = json.loads(js)
link = jsl["url"][0]["url"]
size = jsl["url"][0]["size"]/(1024*1024)
print(u'视频大小:%s MB，请按任意键下载' %size)
raw_input()
download(link)

