# !C:\Users\enjoy\AppData\Local\Programs\Python\Python38\python.exe
# -*- coding: utf-8 -*-
import sys

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
        [sg.Text('プロジェクトファイル', size=(20, 1))],
        [sg.Input(key='project-file')],
        [sg.FileBrowse('選択', key='project-file', file_types=(("プロジェクトファイル", ".ymmp"),))]
    ]

    window = sg.Window(Var.TITLE, layout, icon=icon, resizable=False, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '終了':
            break

    window.close()

if __name__ == '__main__':
    icon = Var.BASE64_ICON
    main()





