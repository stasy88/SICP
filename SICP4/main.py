import math

class Rational:
    def __init__(s,n,d):
        s.n = n
        s.d = d
    def __add__(s,o):
        new_n = s.n*o.d + o.n*s.d
        new_d = s.d*o.d
        return Rational(new_n,new_d)
    def simplify(s):
        gcd = math.gcd(s.n,s.d)
        s.n //= gcd
        s.d //= gcd
    def __str__(s):
        if s.n % s.d == 0:
            return str(s.n // s.d)
        elif abs(s.n) > s.d:
            whole = s.n // s.d
            rem = abs(s.n) % s.d
            return f"{whole}({rem}/{s.d})"
        else:
            return f"{s.n}/{s.d}"

def make_rat(n,d):
    return Rational(n,d)
def numer(x):
    g = math.gcd(x.n,x.d)
    return x.n // g
def denom(x):
    g = math.gcd(x.n,x.d)
    return x.d // g
def rational(str):
    while True:
        try:
            n,d = map(int,str.split('/'))
            if d == 0:
                raise ValueError()
            return make_rat(n,d)
        except ValueError:
            print("Ошибка: некорректный ввод")
            return None

while True:
    s_nums = input("\nВведите числа разделенные пробелами: ")
    l_nums = s_nums.split()
    nums = []

    for num in l_nums:
        rat = rational(num)
        if rat is not None:
            nums.append(rat)
        else:
            nums = []
            break
    if nums:
        result = sum(nums, make_rat(0,1))
        result.simplify()
        print("Результат:", result)

        proc = input("\nПродолжить? - ")
        if proc.lower() in ('no','нет'):
            break
    else:
        continue