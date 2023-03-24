# def sum_num(n):
#     summa=0
#     for i in range(1,n+1):
#         summa+=i
#     return summa
# print(sum_num(5))

# def sum_str(*args):
#     res=''
#     for i in args:
#         res+=str(i)
#     return res
# print(sum_str(1,2,5))

# import modul1

# print(modul1.max_num(5,9))

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1=[]
for i in range(1,10):
    list_1.append(fib(i))
print(list_1)