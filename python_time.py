import loop
import timeit


def keisoku():
    
    N = 1000000
    sum = 0
    for i in range(N):
        sum += i
print(timeit.timeit(keisoku,number=1000))

