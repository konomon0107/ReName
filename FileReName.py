import bs4
import webview
import tkinter as tk
from tkinter import filedialog
import os
import glob
import datetime
from natsort import natsorted

soup = bs4.BeautifulSoup(open('./FileReName.html',encoding='utf-8'),'html.parser',)

class Api:
    def __init__(self):
        self.name = 'js_api'

    def get_folder(self):
        # ルートウィンドウを作成し、そこにファイルダイアログをのせる
        root = tk.Tk()
        root.withdraw()
        idir = 'C:\\'
        FolderName = filedialog.askdirectory(initialdir = idir)
        respose = {
            'message' : FolderName,
            }
        print(respose)
        # ルート要素を削除しなければダイアログボックスが2回目以降開けない
        root.destroy()
        return respose

    def execution(self,folder_name,file_name,f,ex,sr):
        path = folder_name + "/*" + ex
        befor_file_list = list(glob.glob(path))
        if sr == "c":
            befor_file_list.sort(key=os.path.getctime)
        elif sr == "m":
            befor_file_list.sort(key=os.path.getmtime)
        else:
            befor_file_list = natsorted(befor_file_list)

        count = len(befor_file_list)
        print(count)
        print('変更前データ')
        print(befor_file_list)

        ymd = datetime.datetime.now().strftime('%Y%m%d')
        print('年月日')
        print(ymd)
        ymdhms = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print('年月日時刻')
        print(ymdhms)

        if f == '1':
            for i, filename in enumerate(befor_file_list, 1):
                rename_path = folder_name + '/' + file_name + '_' + str(i) + ex
                os.rename(filename,rename_path)
                message = '連番形式で' + str(count) + '件のファイル名を変更しました。'
        elif f == '2':
            for i, filename in enumerate(befor_file_list, 1):
                trg_filename_all = filename.split('\\')[1]
                trg_filename = trg_filename_all.split('.')[0]
                rename_path = folder_name + '/' + trg_filename + '_' + ymd + ex
                os.rename(filename,rename_path)
                message = '年月日形式で' + str(count) + '件のファイル名を変更しました。'
        elif f == '3':
            for i, filename in enumerate(befor_file_list, 1):
                trg_filename_all = filename.split('\\')[1]
                trg_filename = trg_filename_all.split('.')[0]
                rename_path = folder_name + '/' + trg_filename + '_' + ymdhms + ex
                os.rename(filename,rename_path)
                message = '年月日時刻形式で' + str(count) + '件のファイル名を変更しました。'
        else:
            message = '表示形式の判定でマッチするものがみつかりませんでした。'
        after_file_list = glob.glob(path)
        print('変更後')
        print(after_file_list)
        response = {
            'message' : message
        }
        return response

if __name__ == '__main__':
    html = str(soup)
    api = Api()
    window = webview.create_window('ファイル名一括変更', js_api=api ,html=html,width=550 ,height=700)
    webview.start()