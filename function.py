# -*- coding: utf-8 -*-

import os
import sys

import shutil
import PySimpleGUI as sg

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

def checkYmmp(path):
    if len(path) == 0:
        sg.popup('ファイルを選択してください', path)
        return False
    elif os.path.exists(path) != True:
        sg.popup('ファイルが間違えています', path)
        return False
    else:
        return True