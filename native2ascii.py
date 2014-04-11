#coding: utf-8
"""
转换文件中unicode编码为ascii码表示
"""
__author__ = 'erawtfos'

import os
import re

BASE_DIR = os.path.dirname(__file__)


def transcoding(file=""):
    """
    转换unicode编码为ascii码表示
    :param file: 要转换的文件路径
    """
    outfile = file.replace(".properties", "_zh_CN.properties")
    with open(file, "rb")as f:
        with open(outfile, "wb") as out:
            for line in f.readlines():
                text = ascii(line.decode().replace('\n', ""))
                text = re.sub("^'|'$|\"$|^\"", "", text)
                out.write(text.encode())
                out.write(b"\n")


def abspath(path="", ExtName=""):
    """
    获取指定目录中完整的文件路径
    :param path: 路径
    :param ExtName: 文件扩展名
    :return: 返回完整路径列表
    """

    list = os.listdir(path)
    pathlist = []
    for filename in list:
        curpath = os.path.join(path, filename)
        if curpath.endswith(ExtName):
            pathlist.append(curpath)
    return pathlist


if __name__ == '__main__':
    path = os.path.join(BASE_DIR, "messages")  #要转换文件所在文件夹
    for i in abspath(path, ".properties"):
        transcoding(i)

