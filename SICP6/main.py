from abc import ABC, abstractmethod

def empty():
    return Nas(15,20,1000,9.81,0.7,2)

class Nas_cen(ABC):
    def __init__(s,V,t,p,g,n,z):
        s.V = V
        s.t = t
        s.p = p
        s.g = g
        s.n = n
        s.z = z
    @abstractmethod
    def Nas_r(s):
        pass
    @abstractmethod
    def Nas_m(s):
        pass

class Nas(Nas_cen):
    def Nas_r(s):
        return s.V/s.t, "м3/с"
    def Nas_m(s):
        return s.p*s.g*s.V/s.t*s.n, "Вт"

nas = empty()
print("\nПарам. центроб. насоса:")
print("\nРасход:", nas.Nas_r())
print("Мощность:", nas.Nas_m(), "\n")

# Особенность программы на Python - использование модуля
# abc для создания абстрактных классов и методов. Определяются
# интерфейсы в подклассах, подчёркивается структура кода.