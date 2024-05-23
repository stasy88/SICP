def curry(func, *args):
    def curried(*more_args):
        return func(*args, *more_args)
    return curried

def power(base, exp):
    return base ** exp

while True:
    a = float(input("\nОснов. степени: "))
    while True:
        n = float(input("Показ. степени: "))
        if (a<0 and (-1<n<0 or 0<n<1)) or (a==0 and n<0):
            print("Значение неопределено\n")
        else:
            break
    curry_power = curry(power, a)
    if curry_power(n).is_integer():
        print("Результат:", int(curry_power(n)))
    else:
        print("Результат:", curry_power(n))
    proc = input("\nПродолжить? - ")
    if proc.lower() in ('no','нет'):
        break