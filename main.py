# !C:\Users\enjoy\AppData\Local\Programs\Python\Python38\python.exe
# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

import Var
import function as func

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('bar.ico')))

    func.makeResouceFiles()

    layout = [
        [sg.Text('プロジェクトファイル', size=(20, 1))],
        [sg.Input(key='project-file')],
        [sg.FileBrowse('選択', key='project-file', file_types=(("プロジェクトファイル", ".ymmp"),))]
    ]

    window = sg.Window(Var.TITLE, layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '終了':
            break

    window.close()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()





