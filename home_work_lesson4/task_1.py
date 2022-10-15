# 1. Вычислить число c заданной точностью d
import decimal
from decimal import Decimal, getcontext

num = decimal.Decimal(input())
print('Дано число: ', num)

n = int(input())
getcontext().prec = 5
numm = Decimal(num)
print(num.quantize(Decimal('1.00')))
