import math 


class Figura():
    
    def area(self):
        pass
    
    def perimetro(self):
        pass


class rectangulo(Figura):

    
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, nueva_base):
        self.__base = nueva_base


    @property
    def altura(self):
        return self.__altura  

    @altura.setter
    def altura(self, nueva_altura):
        self.__altura = nueva_altura              
    
    
    def area(self):
        return self.__base * self.__altura


    
    def perimetro(self):
        return (self.__base + self.__altura) * 2     
    

    
        


class cuadrado(rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)
    



class circulo(Figura):

    def __init__(self,radio):
        self.__radio = radio



    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, nuevo_radio):
        self.__radio = nuevo_radio
    
    

    def area(self):
        return math.pi * (self.__radio**2)
    

    def perimetro(self):
        return 2 * math.pi * self.__radio 



class triangulo(Figura):
    
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, nueva_base):
        self.__base = nueva_base


    @property
    def altura(self):
        return self.__altura  

    @altura.setter
    def altura(self, nueva_altura):
       self.__altura = nueva_altura              
    
    
    def area(self):
        return (self.__base * self.__altura) / 2


    
    def perimetro(self):
        return self.__base * 3  



Rectangulo = rectangulo(3,4)        
Cuadrado = cuadrado(7)
Circulo = circulo(4)
Triangulo = triangulo(5, 7)


print('Rectangulo --> Area:' + str(Rectangulo.area()) + '  Perimetro: ' + str(Rectangulo.perimetro()))
print('Cuadrado --> Area:' + str(Cuadrado.area()) + '  Perimetro: ' + str(Cuadrado.perimetro()))
print('Circulo --> Area:' + str(Circulo.area()) + '  Perimetro: ' + str(Circulo.perimetro()))
print('Triangulo --> Area:' + str(Triangulo.area()) + '  Perimetro: ' + str(Triangulo.perimetro()))