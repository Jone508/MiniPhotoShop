"""
by: cjh
time:2022/1/5
gitee:https://gitee.com/jone508/openc-curriculum.git
"""

# 常量的定义
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600


class Variable:
    # 全局变量
    image = None
    imagelabel = None
    width = 0
    height = 0


def set_width(value):
    Variable.width = value


def get_width():
    return Variable.width


def set_height(value):
    Variable.height = value


def get_height():
    return Variable.height


def set_image(image):
    Variable.image = image


def get_image():
    return Variable.image


def set_imagelabel(imagelabel):
    Variable.imagelabel = imagelabel


def get_imagelabel():
    return Variable.imagelabel
