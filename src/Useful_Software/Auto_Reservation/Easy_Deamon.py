#5秒ごとに日時をtxtファイルに(練習のため5回)印字するプログラムを作成
import daemon
import os
import time
from datetime import datetime

class EasyDaemon:

    def __init__(self):
        self.txtdir = os.path.expanduser("~/Python_src/src/Useful_Software/Auto_Reservation/") #ディレクトリの指定
        self.txtpath = os.path.join(self.txtdir,"date.txt") #ファイル名の指定
        self.i = 0

    def run(self):
         while True:
            print( "pid: %d, ppid: %d, time: %s" % (os.getpid(), os.getppid(), datetime.now()) )
            time.sleep(5)
            self.i = self.i + 1
            if self.i == 5:
                print("%d 回実行しました" % self.i)
                break

def main():
    std_daemon = EasyDaemon()
    context = daemon.DaemonContext(working_directory = std_daemon.txtdir,
                                   stdout = open("stdout_file.txt", "w+"), #標準出力先を変更する.（つまり標準出力ではない)
                                   stderr = open("stderr_file.txt", "w+")) #標準エラー出力先を変更する.
    with context:
        std_daemon.run()

if __name__ == '__main__':
    main()
