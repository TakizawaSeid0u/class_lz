from octagon import Octagon

# Задаем объект
oct = Octagon(10)

# Вывод вычислений на экран
print("Радиус описанной окружности:", oct.CC_R())
print("Площадь описанной окружности:", oct.CC_A())
print("Радиус вписанной окружности:", oct.IC_R())
print("Площадь вписанной окружности:", oct.IC_A())
print("Площадь октогона:", oct.area())
print("Периметр октогона:", oct.p())

oct.draw() # Отрисовываем