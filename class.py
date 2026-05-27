class Car :
    def __init__(self):
        self.__color = "red"
        self.__model = "BMW"
        self.__year = 2020  
        
        
    def get_color(self):
            return self.__color
        
        
        
car1 = Car()
print(car1.get_color())