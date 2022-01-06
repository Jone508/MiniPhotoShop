"""
by: cjh
time:2022/1/5
gitee:https://gitee.com/jone508/openc-curriculum.git
"""

from PIL import ImageEnhance, ImageDraw, ImageFont

from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
import Variable


class Process():
    # 修改类
    imagelabel = Variable.get_imagelabel()


    def __init__(self):
        self.bright = 1
        self.sharpness = 1
        self.contrast = 1
        self.cont = 1
        self.shar = 1
        self.angle = 0
        self.height = 0
        self.width = 0
        self.watermark = False
        self.beautify = False
        self.deathmark = False
        self.save = ""

    # 改变属性值的函数
    def change_bright(self, bright):
        self.bright = bright
        
    def change_shar(self, shar):
        self.shar = shar

    def change_width(self, value):
        self.width = Variable.get_width() + value

    def change_height(self, value):
        self.height = Variable.get_height() + value

    def change_angle(self, angle):
        self.angle = angle

    def change_watermark(self):
        self.watermark = not self.watermark
    
    def change_beautify(self,image):
        self.beautify = not self.beautify
        
    def change_death(self,image):

        self.deathmark = not self.deathmark


    def get_watermark(self):
        return self.watermark
    def get_beautify(self):
        return self.beautify
    def get_deathmark(self):
        return self.deathmark
    

    def change_save(self, path):
        self.save = path

    def process_photo(self,image):

        # 应用修改
        if image is not None:
            enhancer = ImageEnhance.Brightness(image)   # 获取图片亮度
            image = enhancer.enhance(self.bright)   # 修改图片亮度

            if self.watermark:
                idraw = ImageDraw.Draw(image)   # 添加水印
                # 设置水印内容
                text = "CJH2019030002086"
                font = ImageFont.truetype("arial.ttf", size=100)
                idraw.text((10, 10), text, font=font)
                
            if self.beautify:
                enhancer = ImageEnhance.Brightness(image)
                image = enhancer.enhance(self.bright+0.05)
                
            if self.deathmark:
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(self.cont+1)   # 修改图片对比度
                enhancer2 = ImageEnhance.Sharpness(image)
                image = enhancer2.enhance(self.shar+0.5)   # 修改图片锐度
            
            
            # 应用图片旋转
            image = image.rotate(self.angle)            
            # 显示图片修改效果
            imagelabel = Variable.get_imagelabel()
            qimg = ImageQt(image)
            img_pix = QPixmap.fromImage(qimg, Qt.AutoColor)
            img_pix = img_pix.scaled(self.width, self.height)   
            imagelabel.setPixmap(img_pix)

            
            if self.save:
                img_pix.save(self.save)
                self.save = False
