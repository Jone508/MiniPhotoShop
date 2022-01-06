"""
by: cjh
time:2022/1/5
gitee:https://gitee.com/jone508/openc-curriculum.git
"""

from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QPushButton, QHBoxLayout, QVBoxLayout
import argparse
from Process import *
import cv2

image = Variable.get_image()
imageLabel = Variable.get_imagelabel()
process = Process()


class AdjustTab(QWidget):
    # 自定义的控件
    def __init__(self):
        # 初始化界面
        super().__init__()
        # 加入亮度调整部分
        self.bright_label = QLabel("亮度") 
        self.bright_label_value = QLabel('0')  
        self.bright_slider = QSlider(Qt.Horizontal, self)   
        # 设置滑动条最大最小值，下同
        self.bright_slider.setMaximum(100)
        self.bright_slider.setMinimum(-100)
        self.bright_slider.setValue(0) 
        self.bright_slider.valueChanged[int].connect(self.changeImage)  
        
        # 加入角度调整部分
        self.rotation_label = QLabel("旋转")
        self.rotation_label_value = QLabel('0')
        self.rotation_slider = QSlider(Qt.Horizontal, self)
        self.rotation_slider.setMaximum(180)
        self.rotation_slider.setMinimum(-180)
        self.rotation_slider.setValue(0)
        self.rotation_slider.valueChanged[int].connect(self.changeImage) 
        
        # 加入高度调整部分
        self.high_label = QLabel("宽")
        self.high_label_value = QLabel('0')
        self.high_slider = QSlider(Qt.Horizontal, self)
        self.high_slider.setMaximum(100)
        self.high_slider.setMinimum(-100)
        self.high_slider.setValue(0)
        self.high_slider.valueChanged[int].connect(self.changeImage)
        
        # 加入宽度调整部分
        self.width_label = QLabel("长")
        self.width_label_value = QLabel('0')
        self.width_slider = QSlider(Qt.Horizontal, self)
        self.width_slider.setMaximum(100)
        self.width_slider.setMinimum(-100)
        self.width_slider.setValue(0)
        self.width_slider.valueChanged[int].connect(self.changeImage)
        
        # 加入重置部分
        self.reset_button = QPushButton("重置亮度")  
        self.reset_button.clicked.connect(self.reset)   
        self.bind_button = QPushButton("重置大小")  
        self.bind_button.clicked.connect(self.resize)   
        self.rerotation_button = QPushButton("重置角度")    
        self.rerotation_button.clicked.connect(self.rerotation)  
        self.watermark_button = QPushButton("添加水印")  
        self.watermark_button.clicked.connect(self.add_watermark)   
        self.beautify_button = QPushButton("一键美颜")  
        self.beautify_button.clicked.connect(self.beautify)   
        self.death_button = QPushButton("一键滤镜")  
        self.death_button.clicked.connect(self.deathmark)  
        
        

        # 款式布局
        # 水平部分
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.bright_label)
        hbox1.addWidget(self.bright_label_value)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.rotation_label)
        hbox2.addWidget(self.rotation_label_value)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.high_label)
        hbox3.addWidget(self.high_label_value)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.width_label)
        hbox4.addWidget(self.width_label_value)
        hbox5 = QHBoxLayout()
        hbox5.addStretch()
        hbox5.addWidget(self.reset_button)
        hbox5.addStretch()
        hbox5.addWidget(self.bind_button)
        hbox5.addStretch()
        hbox5.addWidget(self.rerotation_button)
        hbox5.addStretch()
        hbox5.addWidget(self.watermark_button)
        hbox5.addStretch()
        hbox5.addWidget(self.beautify_button)
        hbox5.addStretch()
        hbox5.addWidget(self.death_button)
        hbox5.addStretch()
        # 垂直部分
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.bright_slider)        
        vbox.addLayout(hbox2)
        vbox.addWidget(self.rotation_slider)
        vbox.addLayout(hbox3)        
        vbox.addWidget(self.high_slider)
        vbox.addLayout(hbox4)
        vbox.addWidget(self.width_slider)
        vbox.addLayout(hbox5)
        self.setLayout(vbox)

    def changeImage(self, value):
        # 改变参数事件    
        image = Variable.get_image()
        # 获取修改参数
        source = self.sender()  
        if source == self.bright_slider:
            # 修改亮度
            self.bright_label_value.setText(str(value))  
            bright = (self.bright_slider.value() + 100) / 100   
            process.change_bright(bright)   
        elif source == self.rotation_slider:
            # 修改角度
            self.rotation_label_value.setText(str(value))
            angle = self.rotation_slider.value()
            process.change_angle(angle)
        elif source == self.high_slider:
            # 修改高度
            self.high_label_value.setText(str(value))
            high = self.high_slider.value()
            process.change_height(high)
        elif source == self.width_slider:
            # 修改宽度
            self.width_label_value.setText(str(value))
            width = self.width_slider.value()
            process.change_width(width)

        # 应用修改
        process.process_photo(image)

    def reset(self):
        # 重置亮度事件
        self.bright_slider.setValue(0) 
        
    def rerotation(self):
        # 重置角度事件
        self.rotation_slider.setValue(0)

    def resize(self):
        # 重置大小事件
        self.width_slider.setValue(0)
        self.high_slider.setValue(0)



    def add_watermark(self):
        # 添加水印事件
        image = Variable.get_image()
        process.change_watermark()  
        process.process_photo(image)    

        # 修改按钮显示内容
        if process.get_watermark():
            self.watermark_button.setText("取消水印")
        else:
            self.watermark_button.setText("添加水印")

    def beautify(self):
        # 添加美颜事件
        image = Variable.get_image()
        process.change_beautify(image)  
        process.process_photo(image)    

        # 修改按钮显示内容
        if process.get_beautify():
            self.beautify_button.setText("取消美颜")
        else:
            self.beautify_button.setText("一键美颜")
            
    def deathmark(self):
        # 添加滤镜事件
        image = Variable.get_image()
        process.change_death(image)  
        process.process_photo(image)    


        # 修改按钮显示内容
        if process.get_deathmark():
            self.death_button.setText("取消滤镜")
        else:
            self.death_button.setText("一键滤镜")