"""
by: cjh
time:2022/1/5
gitee:https://gitee.com/jone508/openc-curriculum.git
"""

import sys
import os

from PIL import Image
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTabWidget, QMainWindow, QAction, QFileDialog, QMessageBox, QMenu, QDesktopWidget, QApplication

from Box import *


class MyTab(QTabWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent        
        self.adjust_tab = AdjustTab()
        # 添加自定义组件
        self.addTab(self.adjust_tab, "工具栏")    
        self.setMaximumHeight(300)      



class PS(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()  

    def initUI(self):
        # 初始化界面
        
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        # 设置菜单栏
        # 新建打开动作
        openAct = QAction('打开', self)  
        openAct.setShortcut('Ctrl+O')   
        openAct.setStatusTip('打开文件')    
        openAct.triggered.connect(self.openImage)   
        # 新建保存动作
        saveAct = QAction('保存', self)  
        saveAct.setShortcut('Ctrl+S')   
        saveAct.setStatusTip('保存文件')    
        saveAct.triggered.connect(self.SaveEvent)   
        # 新建退出动作
        exitAct = QAction('退出', self)  
        exitAct.setShortcut('Esc')  
        exitAct.setStatusTip('退出软件')    
        exitAct.triggered.connect(self.close)   
        #新建信息窗口
        cjhAct = QAction('作者：陈景豪',self)
        cjhAct2 = QAction('学号：2019030002086',self)
        

        # 新建一个菜单栏内
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')  # 设置菜单栏显示的内容
        myMenu = menubar.addMenu('关于作者')
        myMenu.addAction(cjhAct)
        myMenu.addAction(cjhAct2)
        # 加入上述三个事件
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

 

        # 修改操作部分
        self.mytab = MyTab(self)    
        # 图片显示部分
        imagelabel = QLabel("") 
        
        vbox = QVBoxLayout()

        vbox.addWidget(self.mytab)
        vbox.addWidget(imagelabel)        
        main_frame = QWidget()
        main_frame.setLayout(vbox)
 
        Variable.set_imagelabel(imagelabel)  
        imagelabel.setAlignment(Qt.AlignCenter) 
        
        
        self.setCentralWidget(main_frame)
        self.resize(Variable.WINDOW_WIDTH, Variable.WINDOW_HEIGHT)  
        self.center()   
        self.setWindowTitle('简易PS-cjh')   
        self.setWindowIcon(QIcon('')) 
        self.show()  

    def openImage(self):
        # 打开文件事件
        imagelabel = Variable.get_imagelabel()  

        path = os.getcwd()  # 获取当前目录
        fname, _ = QFileDialog.getOpenFileName(
            self, '打开图片', path, "Image files (*.jpg *.png)")  
        if fname:   
            image = Image.open(fname)  
            Variable.set_image(image)  
            self.mytab.adjust_tab.reset()
            self.mytab.adjust_tab.resize()
            self.mytab.adjust_tab.rerotation()
            # 呈现图片
            qimg = ImageQt(image)   
            img_pix = QPixmap.fromImage(
                qimg, Qt.AutoColor) 
            img_pix = img_pix.scaled(
                Variable.DEFAULT_WIDTH, Variable.DEFAULT_HEIGHT, Qt.KeepAspectRatio)    # 将QPixmap按图片比例调整大小至可放入QLabel
            imagelabel.setPixmap(img_pix)   # 放入QLabel
            # 将此时的长宽存入全局变量
            Variable.set_width(img_pix.width())
            Variable.set_height(img_pix.height())
           
            process.change_width(0)
            process.change_height(0)
        else:
            pass

    def closeEvent(self, event):
        # 关闭软件事件
        reply = QMessageBox.question(self, '提示',
                                     "你确定要退出吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)    

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def SaveEvent(self):
        # 保存文件事件
        path = os.getcwd()  
        filename, _ = QFileDialog.getSaveFileName(
            self, "文件保存", path, "Image files (*.jpg *.png)")
        if filename:
            image = Variable.get_image()    
            process.change_save(filename)   
            process.process_photo(image)    
        else:
            pass

    def contextMenuEvent(self, event):
        # 菜单内容
        cmenu = QMenu(self)

        opnAct = cmenu.addAction("打开")
        saveAct = cmenu.addAction("保存")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == opnAct:
            self.openImage()
        if action == saveAct:
            self.SaveEvent()

    def center(self):
        # 设置屏幕居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ex = PS()  
    sys.exit(app.exec_())     
  

