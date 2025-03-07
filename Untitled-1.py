#импортим необходимые библиотеки
import math 
import matplotlib.pyplot as plt 
import numpy as np 

class Octagon: #созадем класс октагона
    def __init__(self, side): #задаем атрибуты октагону
        self.side = side #сторона октагона
        self.angle = 135  # угол
        self.k = 1 + math.sqrt(2) # Константа k

    def CC_R(self): #метод для радиуса описанной окружности
        "Радиус описанной окружности"
        return self.side/ (2 * math.sin(math.pi / 8))  
    
    def CC_A(self): #метод для площади описанной окружности
        "Площадь описанной окружности"
        r = self.CC_R()
        return math.pi * r**2
    
    def IC_R(self): #метод для радиуса вписанной окружности
        "Радиус вписанной окружности"
        return self.side/(2 * math.tan(math.pi / 8))  
    
    def IC_A(self): #метод для площади вписанной окружности
        "Площадь вписанной окружности"
        r = self.IC_R()
        return math.pi * r**2
    
    def area(self): #метод для площади октагона
        "Площадь октагона"
        return 2*self.side**2*(1 + math.sqrt(2))
    
    def p(self):
        "Периметр октагона"
        return self.side*8
    
    def draw(self):
        fig, ax = plt.subplots(figsize=(15, 15))
        ax.set_aspect('equal')

        R_out = self.side/ (2 * math.sin(math.pi / 8))  
        R_in = self.side/(2 * math.tan(math.pi / 8))
        
        x = [R_out * math.cos(i * np.pi/4) for i in range(8)]
        y = [R_out * math.sin(i * np.pi/4) for i in range(8)]

        """theta = np.linspace(0, 2 * np.pi, 9)[:-1] + np.pi / 8
        x = self.side * np.cos(theta) * self.k / 2
        y = self.side * np.sin(theta) * self.k / 2"""
        
        ax.fill(x, y, color='black', label='Октагон')

        r_circ = self.CC_R() #Описанная окружность
        circle_circ = plt.Circle((0,0), r_circ, color="blue", fill=False, label="Описанная окружность")
        ax.add_patch(circle_circ)

        r_in = self.IC_R() #вписанная окружность
        circle_in = plt.Circle((0,0), r_in, color="red", fill=False, label="Вписаннная окружность")
        ax.add_patch(circle_in)


        plt.legend()
        plt.grid()
        plt.show()