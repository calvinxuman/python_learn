# -*- coding: utf-8 -*-

#给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen():
    #__slots__ = ('width','height','resolution')

    # def __init__(self,width,height):
    #     self.__width = width
    #     self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        if not isinstance(width,int):
            raise ValueError('width must be an integer!')
        if width < 0 or width > 1920:
            raise ValueError('width must between 0 ~ 1920!')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        if not isinstance(height,int):
            raise ValueError('height must be an integer!')
        if height < 0 or height > 1080:
            raise ValueError('height must between 0 ~ 1080!')
        else:
            self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height

s = Screen()
s.width = 1920
s.height = 1080
print('resolution =', s.resolution)






