import random

def fibonacci(n):
    fibo = []
    fibo.append(0)
    fibo.append(1)
    for i in range(2,n + 1):
        summ=fibo[i - 1] + fibo[i - 2]
        fibo.append(summ)
    print("The Series:" ,fibo)
    return fibo[n]





n = int(input())
#n = random.randrange(2,20000)
print(n)
fibResult = fibonacci(n)
print("Result:",fibResult)
