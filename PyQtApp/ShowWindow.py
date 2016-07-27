import sys
from PyQt4 import QtGui

# http://myenigma.hatenablog.com/entry/2016/01/24/113413#はじめに

def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(250, 150)
    w.setWindowTitle('QtSample')
    w.setWindowIcon(QtGui.QIcon('pythonlogo.png'))  #アプリケーションアイコンを設定 (Pythonのロゴ)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()