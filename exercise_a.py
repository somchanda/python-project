# A1
print('\n\nA1:')
for i in range(14):
    print('*', end='')

# A2
print('\n\nA2:')
for i in range(4):
    for j in range(14):
        print('*', end='')
    print('')

# A3
print('\n\nA3:')
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print('')

# A4
print('\n\nA4:')
for i in range(1, 6):
    for j in range(pow(2, i - 1)):
        print('*', end='')
    print('')

# A5
print('\n\nA5:')
for i in range(1, 6):
    for j in range(0, 5 - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

# A6
print('\n\nA6:')
n = 0
r = 5
for m in range(1, r + 1):
    for gap in range(1, (r - m) + 1):
        print(' ', end="")
    while n != (2 * m - 1):
        print("*", end="")
        n = n + 1
    n = 0
    print()

# A7
print('\n\nA7:')
for i in range(1, 10):
    for j in range(i, 0, -1):
        print(j, end='')
    print()

# A8
print('\n\nA8:')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# A9
print('\n\nA9:')
for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()

# A10
print('\n\nA10:')
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# A10
print('\n\nA10:')
r = 7
for i in range(r + 1):
    for gap in range(0, (r - i)):
        print(' ', end='')
    for j in range(i - 1, -1, -1):
        print(j, end='')
    for k in range(1, i):
        print(k, end='')
    print()

# B
# print('\n\nB:')
# import cmath
# print("The standard form of a quadratic equation is: ", end='')
# print("ax^2 + bx + c = 0")
# a = input('Enter a: ')
# b = input('Enter b: ')
# c = input('Enter c: ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = (b**2) - (4*a*c)
# sol1 = (-b - cmath.sqrt(d))/(2*a)
# sol2 = (-b + cmath.sqrt(d))/(2*a)
# print('The solution are {0} and {1}'.format(sol1, sol2))

# C
# print('\n\nC:')
# def cal_math_operation(n, m):
#     print("N + M = ", n + m)
#     print("N * M = ", n * m)
#     if m != 0:
#         print("N / M = ", n / m)
#     print("N - M = ", n - m)
# n = input('Enter n: ')
# m = input('Enter m: ')
# cal_math_operation(int(n), int(m))

# D
# print('\n\nD:')
# def factorial(n):
#     if n ==1:
#         return n
#     elif n < 1:
#         return "NA"
#     else:
#         return n * factorial(n-1)
# n = input('Enter n: ')
# print("Factorial of {0} is: {1}" .format(n, factorial(int(n))))

# E
# print('\n\nE:')
# def check_value(n):
#     n = int(n)
#     if n % 2 == 0:
#         print("{0} is even number" .format(n))
#     else:
#         print("{0} is odd number" .format(n))
# n = input("Enter n: ")
# check_value(n)

# F
# print('\n\nF:')
# def my_sum(data):
#     total = 0
#     for d in data:
#         total += d
#     return total
# n = input("Enter number of list: ")
# n = int(n)
# data = list()
# for i in range(n):
#     val = input('Enter val[{0}] : ' .format(i))
#     data.append(int(val))
# print('Sum = ', my_sum(data))

# G
print('\n\nG: ')
# def statistic(data):
#     n = len(data)
#     get_sum = sum(data)
#     mean = get_sum / n
#     data.sort()
#
#     if n % 2 == 0:
#         median1 = data[n // 2]
#         median2 = data[n // 2 - 1]
#         median = (median1 + median2) / 2
#     else:
#         median = data[n // 2]
#     return [get_sum, mean, median]
#
# n = input("Enter number of list: ")
# n = int(n)
# data = list()
# for i in range(n):
#     val = input('Enter val[{0}] : ' .format(i))
#     data.append(int(val))
# print(statistic(data))

# K
print('\n\nK: ')
from tabulate import tabulate
from datetime import datetime, timedelta
import calendar
loan = input('Enter loan ($): ')
rate = input('Enter interest rate(%): ')
duration = input('Enter duration(monthly): ')
dateReceive = input('Enter date receive (dd-mm-YYYY): ')
dateReceive = datetime.strptime(dateReceive, '%d-%m-%Y')
datePayment = input('Enter date to start payment(dd-mm-YYYY): ')
datePayment = datetime.strptime(datePayment, '%d-%m-%Y')
loan = float(loan)
rate = float(rate)
duration = int(duration)
# To calculate interest
interest = loan * rate / 100
repayment = loan / duration
# To increase date 1 month
dayInMonth = calendar.monthrange(dateReceive.year, dateReceive.month)[1]
print(dateReceive + timedelta(days=dayInMonth))
data = list()

for i in range(1, int(duration + 1)):
    if i == 1:
        data.append(
            {'Period': i, 'date': str(datePayment.strftime('%d-%m-%Y')), 'loan': loan, 'interest': round(interest, 2),
             'repayment': round(repayment, 2), 'totalRepayment': round(interest + repayment, 2)})
    else:
        dayInMonth = calendar.monthrange(datePayment.year, datePayment.month)[1]
        date = datetime.strptime(data[i - 2]['date'], '%d-%m-%Y')
        date = date + timedelta(days=dayInMonth)
        date = date.strftime('%d-%m-%Y')
        data.append({'Period': i, 'date': date, 'loan': round(data[i-2]['loan'] - data[i-2]['repayment'], 2), 'interest': 0, 'repayment': round(repayment, 2), 'totalRepayment': 0})
        data[i-1]['interest'] = round(data[i-1]['loan'] * rate / 100, 2)
        data[i-1]['totalRepayment'] = round(data[i-1]['interest'] + repayment, 2)



if datePayment.weekday() == 5:
    datePayment = datePayment + timedelta(days=2)
if datePayment.weekday() == 6:
    datePayment = datePayment + timedelta(days=1)
print(tabulate(data, headers='keys', tablefmt='grid'))