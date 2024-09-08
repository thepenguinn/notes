# stupid me, becasue i am.

def gen(n):
    for i in range(n):
        yield i

g = gen(3)

print(list(g))



