#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Homing
@software: PyCharm Community Edition
@file: day1.py
@time: 2017/5/7 10:48
"""

# Linux软件安装
'''
1. 先cd 到安装包路径
2. unzip解压安装包
3. cd到解压路径
4. ./ 安装脚本
'''
 # Liunx 软件打开

'''
 
 cd 到安装解压文件夹
 
 ./安装脚本
 
 '''
 # Liunx 删除文件/目录
 '''
 rm file_name  删除文件
 
 rm -r document_name 删除文件夹/目录 删除文件夹时。需要一一确认
 
 rm -rf document_name 删除目录时，直接删除，不需要确认
 
 '''
# Liunx 移动文件或者文件夹

'''
mv[option] 源文件/文件夹 目标文件/文件夹

-i 交互式操作 需要确认是否移动
-f 禁止交互操作，不需要确认是否移动
 pwd 查看完整路径
'''
# Liunx 启动服务

'''
sudo service mysql start


'''

# 基本安装
'''
1.pip python安装包管理工具
 a. pip install flask
 b. pip list
 c. pip show flask
d. pip install -i http://pypi.douban.com/simple/flask

2. virtualenv 初始化环境
pip install virtualenv
virtualenv/tem/test
cd /tem/test

source bin/active
deactivate

3. pyenv 当前系统安装不同版本


'''
# 3个小工具
'''
1.启动下载服务器 python -m SimpleHTTPServer
2.转换json   echo '{"job": "developer", "name": "lmx", "sex": "male"}' | python -m json.tool
3.python -c "import module"

'''

# ipython

#json


import json
data = dict(a=1,b2)

t=json.dumps(data)
line = '{"a":1,"b":2}'

json.loads(line)

# jupyter

'''
sudo pip install jupyter
jupyternotebook --no-browser --ip=0.0.0.0


'''


# 作业












