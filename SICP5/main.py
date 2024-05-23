class Kettle:
    def __init__(s, empty=True, on_stove=False, gas_lit=False,
                 tap_water=False, matches=False, gas_stove=False):
        s.empty = empty
        s.on_stove = on_stove
        s.gas_lit = gas_lit
        s.tap_water = tap_water
        s.matches = matches
        s.gas_stove = gas_stove

    def fillWater(s):
        if s.tap_water:
            print("Наполняем чайник водой из-под крана")
            s.empty = False
        else:
            print("Нет доступа к воде из-под крана")

    def putStove(s):
        if s.gas_stove:
            print("Ставим чайник на газовую плиту")
            s.on_stove = True
        else:
            print("Плита не зажжена")

    def lightGas(s):
        if s.matches:
            print("Зажигаем газ на плите")
            s.gas_lit = True
        else:
            print("Нет спичек")

    def boilWater(s):
        if not s.empty and s.on_stove and s.gas_lit:
            print("Ждём, пока вода закипит")
            print("Вода закипела!")
        elif s.empty:
            print("Чайник пуст")
        elif not s.on_stove:
            print("Чайник не на плите")
        elif not s.gas_lit:
            print("Газ не зажжён")

    def pourWater(s):
        if not s.empty:
            print("Выливаем воду из чайника")
            s.empty = True
        else:
            print("Чайник уже пустой")


print()

# Пустой чайник
ket_1 = Kettle()
ket_1.tap_water = True
ket_1.matches = True
ket_1.gas_stove = True
ket_1.fillWater()
ket_1.putStove()
ket_1.lightGas()
ket_1.boilWater()
print()

# Наполненный чайник
ket_2 = Kettle(empty=False,
               on_stove=True, gas_lit=True)
ket_2.pourWater()
ket_1.tap_water = True
ket_1.matches = True
ket_1.gas_stove = True
ket_1.fillWater()
ket_1.putStove()
ket_1.lightGas()
ket_1.boilWater()
print()

# Проверка объекта
ket_3 = Kettle(matches=True)
print("Газ зажжён? -", ket_3.gas_lit)
ket_3.lightGas()
print("Газ зажжён? -", ket_3.gas_lit)
print()