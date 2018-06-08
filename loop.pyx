

def loop(N):
    cdef int sum = 0
    cdef int i
    for i in range(N):
        sum += i
    return sum

def printResult(val):
    print(val)
