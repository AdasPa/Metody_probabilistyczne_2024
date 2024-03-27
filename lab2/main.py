print("ZAD 1")
class RNG_linear:
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed


a = 16.807
c = 0
m = 2**31-1
seed = 10
linear = RNG_linear(a, c, m, seed)
N = 10000

numbers_linear = [linear.generate()/m for _ in range(N)]

r = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for i in numbers_linear:
    h = int(i*10)
    r[h] += 1
print(r)
print(numbers_linear[:30])

r = 1
counter_in = 0
counter_all = 0
area = 0
for i in range(0, len(numbers_linear), 2):
    num1 = 2*numbers_linear[i] - 1
    num2 = 2*numbers_linear[i+1] - 1
    counter_all += 1
    if ((num1**2 + num2**2) < 1) and (((num1-1)**2 + (num2-1)**2) < r**2):
        counter_in += 1

area = (counter_in/counter_all) * 4

print(area)
print()

print("ZAD 2")
class RNG_register:
    def __init__(self, p, q, seed):
        self.p = p
        self.q = q
        self.seed = 2**p + seed

    def generate(self, N):
        numbers = []
        s = bin(self.seed)
        for i in str(s[2:]):
            numbers.append(int(i))
        for i in range(len(str(s)), N + len(str(s))):
            num = numbers[i - self.p] ^ numbers[i - self.q]
            numbers.append(num)
        return numbers[len(str(s)):]

p = 10
q = 3
seed = 897214768658
register = RNG_register(p, q, seed)
N = 10000

numbers_register = register.generate(N)

print(numbers_register[:30])
print(len([i for i in numbers_register if i == 1])/N)

zN = 20
zK = 5

ctr_all = 0
ctr_eagle = 0

for i in range(0, len(numbers_register) - zN, zN):
    pack = numbers_register[i:i+zN-1]
    ctr_all += 1
    are_eagles = False
    for j in range(zN):
        small = pack[j:j+zK]
        if small == [0, 0, 0, 0, 0]:
            are_eagles = True
            ctr_eagle += 1
            break


print(ctr_eagle/ctr_all)
