import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import GUIlast

if __name__=='__main__':
    app=QApplication(sys.argv)  #sys.argv[]就是一个从程序外部获取参数的桥梁

    mainW=QMainWindow()   #建立主程序窗口
    ui=GUIlast.Ui_MainWindow()  #将窗口的内容赋值给ui
    ui.setupUi(mainW)   #创建窗口

    mainW.show()  #将窗口运行出来
    sys.exit(app.exec_()) #防止窗口达成后立刻闪退，以实现程序循环
