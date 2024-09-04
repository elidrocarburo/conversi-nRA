class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

class Suma(Calculadora):
    def __init__(self, num1, num2):
        super().__init__(num1,num2)
    
    def calcular_resultado(self):
        suma = self.num1 + self.num2
        return suma
    
class Resta(Calculadora):
    def __init__(self, num1, num2):
        super().__init__(num1,num2)
    
    def calcular_resultado(self):
        resta = self.num1 - self.num2
        return resta
    
class Multiplicación(Calculadora):
    def __init__(self, num1, num2):
        super().__init__(num1,num2)
    
    def calcular_resultado(self):
        multiplicacion = self.num1 * self.num2
        return multiplicacion
    
class División(Calculadora):
    def __init__(self, num1, num2):
        super().__init__(num1,num2)

    def calcular_resultado(self):
        if self.num2!=0:
            division = self.num1 / self.num2
            return division
        else:
            return "Ingrese un número diferente de cero"

num1= float(input("Ingresa el primer número: "))
signo =input("Ingrese un operador: ")
num2= float(input("Ingresa un segundo número: "))
if signo=="+":
    resultado= Suma(num1,num2)
elif signo=="-":
    resultado= Resta(num1,num2)
elif signo=="*":
    resultado= Multiplicación(num1,num2)
elif signo=="/":
    resultado=División(num1,num2)
else:
    print("Opción inválida, intente de nuevo")

print("El resultado es de: ", resultado.calcular_resultado())