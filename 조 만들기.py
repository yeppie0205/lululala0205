# 조 만들기
import random

t = input("조 만들기 시작")
def jojo():
    i = list(range(1, 14))
    j = list(range(15, 32))
    m = i + j
    random.shuffle(m)
    nn = 0
    t = 10
    q = int((30 / t) + 1)
    for i in range(1, q):
        k = t*i
        print(m[nn: k])
        nn = k 
    
jojo()

