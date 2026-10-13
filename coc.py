import random

def wait_myst(n):
    lst = [1,2,3,4,5,6,7,8,9]
    while True :
        a = random.randint(1,n)
        if a in list:
            return len(lst)+1
        lst.append(a)

print(wait_myst(5))