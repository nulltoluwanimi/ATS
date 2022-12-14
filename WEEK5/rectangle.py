class Rectangle:
    def __init__(self, length=1, breath=1):
        self.__length = length
        self.__breath = breath

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if type(value) != float:
            raise ValueError("length must be a floating number")
        else:
            self.__length = value

    @property
    def breath(self):
        return self.__length

    @breath.setter
    def breath(self, value):
        if type(value) != float:
            raise ValueError("length must be a floating number")
        else:
            self.__length = value

    def perimeter(self):
        return self.__length + self.__breath


    def area(self):
        return self.__length * self.__breath
