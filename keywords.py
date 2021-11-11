
import  keyword
print(keyword.kwlist)

print(True and False)

print(True or False)

print(not False)

import math as myAlias
myAlias.cos(myAlias.pi)
print(myAlias.cos(myAlias.pi))

import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
asyncio.run(main())

for t in range (0,100):
    if t == 98:
        break
    print(t)


    for j in range(9,99):
        if j == 75:
            continue
        print(j)


a = b = 7
del b
print(a)




a = ['x' , 'y' ,'z']
del a[2]
print(a)


def ifexample(a):
    if a == 3:
        print('flush')
    elif a == 5:
        print('yono')
    else:
        print('raise')

ifexample(5)
ifexample(7)
ifexample(4)
ifexample(3)

