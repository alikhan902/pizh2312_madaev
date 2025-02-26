from module import *

#Пример использование
v1 = Vector3D(4, 1, 2)
v1.display()

v2 = Vector3D()
v2.read()

v3 = Vector3D(1, 2, 3)
v4 = v1 + v2
v4.display()

a = v4 * v3
print(a)

v4 = v1 * 10  
v4.display()

v4 = v1 @ v3 
v4.display()
del v4
#Результат