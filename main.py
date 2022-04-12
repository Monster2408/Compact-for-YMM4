# !C:\Users\enjoy\AppData\Local\Programs\Python\Python38\python.exe
# -*- coding: utf-8 -*-
import sys
import os

import PySimpleGUI as sg

import Var
import function as func

def main():
    func.makeResouceFiles()
    
    # This bit gets the taskbar icon working properly in Windows
    if sys.platform.startswith('win'):
        import ctypes
        # Make sure Pyinstaller icons are still grouped
        if sys.argv[0].endswith('.exe') == False:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation') # Arbitrary string

    layout = [
        [sg.Text('プロジェクトファイル')],
        [sg.Input(key='project-file'), sg.FileBrowse('選択', key='project-file', file_types=(("プロジェクトファイル", ".ymmp"),))],
        [sg.Button('読込',key="load-ymmp")],
        [sg.Multiline(size=(100, 50), key='view-ymmp', disabled=True)]
    ]

    window = sg.Window(Var.TITLE, layout, icon=icon, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '終了':
            break
        path = values['project-file']
        if event == "load-ymmp" and func.checkYmmp(path) == True:
            f = open(path, 'r', encoding='UTF-8')
            data = f.read()
            window.FindElement('view-ymmp').Update(data)
            f.close()
        elif event == "ymmp-cymmp" and func.checkYmmp(path) == True:
            print("ymmp-cymmp")

    window.close()

if __name__ == '__main__':
    icon = Var.BASE64_ICON
    main()





