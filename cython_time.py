import loop
import timeit



def keisoku():
    N = 10000
    s = loop.loop(N)

print(timeit.timeit(keisoku,number=1000))
