# -*- coding: utf-8 -*-

import os
import sys

import shutil

def makeResouceFiles():
    """リソースフォルダを作成"""
    if os.path.exists("./resources") != True:
        os.mkdir("./resources")
    if os.path.exists("./resources/data.yml") != True:
        print(resourcePath("resources/data.yml"))
        shutil.copyfile(resourcePath("resources/data.yml"), "./resources/data.yml")

def resourcePath(filename): 
    """内部リソースを取得

    Args:
        filename (string): リソースのファイルpath

    Returns:
        file
    """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(filename)