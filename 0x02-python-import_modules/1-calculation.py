#!/usr/bin/python3
a = 10
b = 5
calculator_1 = __import__('calculator_1')

add_result = calculator_1.add(a, b)
sub_result = calculator_1.sub(a, b)
mul_result = calculator_1.mul(a, b)
div_result = calculator_1.div(a, b)

print("10 + 5 =", add_result)
print("10 - 5 =", sub_result)
print("10 * 5 =", mul_result)
print("10 / 5 =", div_result)
