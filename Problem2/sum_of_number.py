
# def add_numbers(*numbers):
#     sum = 0
#     for num in numbers:
#         sum += int(num)
#     return sum
# x = input()
# y = input()
# z = input()
# q = input()
# print(add_numbers(x,y,z,q))


def add_numbers():
    sum=0
    while (True):
        try:
             num = int(input())
        except ValueError:
            break
        if num!='q':
            sum += int(num)
        else:
            break    
    return sum
print(add_numbers())
