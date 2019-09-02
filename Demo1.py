def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


def fab2(max):
    n, a, b = 0, 0, 1
    l= []
    while n < max:
        l.append(b)
        a, b = b, a + b
        n = n + 1
    return l


for i in fab2(5):
    print(i)


def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for n in fab3(5):
    print(n)
