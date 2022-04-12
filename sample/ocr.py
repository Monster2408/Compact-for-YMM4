import os
import sys
from PIL import Image

import PySimpleGUI as sg
import pyocr
import pyocr.builders


def scan_file_to_str(file_path, langage):
   """read_file_to_str

        画像ファイルから文字列を生成する

        Args:
            file_path(str): 読み取るファイルのパス
            langage(str): 'jpn' または 'eng'

        Returns:
           読み取った文字列
   """
   tools = pyocr.get_available_tools()
   if len(tools) == 0:
      print("No OCR tool found")
      sys.exit(1)

   tool = tools[0]

   text = tool.image_to_string(
      Image.open(file_path),
      lang=langage,
      builder=pyocr.builders.TextBuilder(tesseract_layout=6)
   )
   return text


# テーマを設定
sg.theme('Light Grey1')

layout = [
   # 1行目
   [sg.Text('読み取るファイル(複数選択可)', font=('IPAゴシック', 16))],
   # 2行目
   [sg.InputText(font=('IPAゴシック', 14), size=(70, 10),), sg.FilesBrowse('ファイルを選択', key='-FILES-'),],
   # 3行目
   [sg.Text('読み取る言語', font=('IPAゴシック', 16)), 
   sg.Radio('日本語', 1, key='-jpn-', font=('IPAゴシック', 10)),
   sg.Radio('英語', 1, key='-eng-', font=('IPAゴシック', 10))],
   # 4行目
   [sg.Button('読み取り実行'),],
   # 5行目
   [sg.MLine(font=('IPAゴシック', 14), size=(100,30), key='-OUTPUT-'),]
]

# ウィンドウを取得
window = sg.Window('簡単OCR', layout)

files = []

a = 0

while True:
   event, values = window.read()
   if event == None:
      break

   if event == '読み取り実行':
      files.extend(values['-FILES-'].split(';'))
      language = 'jpn' if values['-jpn-'] else 'eng'
      text = ''
      for i in range(len(files)):
         if not i == 0:
            text += '================================================================================================\n'
         text += scan_file_to_str(files[i], language)
         if language == 'jpn':
            text = text.replace(' ', '')
         text += '\n\n'
      window.FindElement('-OUTPUT-').Update(text)
      sg.Popup('完了しました')

window.close()