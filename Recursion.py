# def show(n):
#     # base case
#     if n==0:
#         return
#     print(n)
#     show(n-1)
#
# show(5)

def fact(n):
    # base case
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


result = fact(6)
print(result)
