#An operator in a programming language is a symbol that tells
# the compiler or interpreter to perform specific mathematical,
# relational or logical operation and produce final result.

# In  python there

#1.Arithmetic operators:
#Def: Arithmetic operators are used to perform mathematical operations
# like addition, subtraction, multiplication , division and Modulus Division.
# +	Addition: adds two operands	x + y
# -	Subtraction: subtracts two operands	x - y
# *	Multiplication: multiplies two operands	x * y
# /	Division (float): divides the first operand by the second	x / y
# //Division (floor): divides the first operand by the second	x // y
#%	Modulus: returns the remainder when first operand is divided by the second	x % y

#2: Relational Operators: Relational operators compares the values.
# It either returns True or False according to the condition.

# >	Greater than: True if left operand is greater than the right	x > y
# <	Less than: True if left operand is less than the right	x < y
# ==	Equal to: True if both operands are equal	x == y
# !=	Not equal to - True if operands are not equal	x != y
# >=	Greater than or equal to: True if left operand is greater than or equal to the right	x >= y
# <=	Less than or equal to: True if left operand is less than or equal to the right	x <= y

# Logical operators: Logical operators perform Logical AND, Logical OR and Logical NOT operations
# and	Logical AND: True if both the operands are true	x and y
# or	Logical OR: True if either of the operands is true	x or y
# not	Logical NOT: True if operand is false	not x

#4.Bitwise operators: Bitwise operators acts on bits and performs bit by bit operation.
# &	Bitwise AND	x & y , binary value of x & Binary Value of y
# |	Bitwise OR	x | y , binary value of x OR binary value of y
# ~	Bitwise NOT	~x  this is 1's complement of -x i.e -x-1
# ^	Bitwise XOR	x ^ y
# >> Bitwise right shift x>> , if x = 1001 then x>> 2 = 0010
# << Bitwise left shift	x<<  similarly x<< 2 = 0100

#5.

# =	Assign value of right side of expression to left side operand	x = y + z
# += Add AND: Add right side operand with left side operand and then assign to left operand	a+=b , a=a+b
# -= Subtract AND: Subtract right operand from left operand and then assign to left operand	a-=b ,a=a-b
# *=	Multiply AND: Multiply right operand with left operand and then assign to left operand a*=b,a=a*b
# /=	Divide AND: Divide left operand with right operand and then assign to left operand	a/=b, a=a/b
# %=	Modulus AND: Takes modulus using left and right operands and assign result to left operand a%=b
#       ,a=a%b
# //=	Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to
#   left operand	a//=b       a=a//b
# **=	Exponent AND: Calculate exponent(raise power) value using operands and assign value
# to left operand	a**=b     a=a**b
# &=	Performs Bitwise AND on operands and assign value to left operand a&=b ,a=a&b
# |=	Performs Bitwise OR on operands and assign value to left operand	a|=b ,a=a|b
# ^=	Performs Bitwise xOR on operands and assign value to left operand	a^=b ,a=a^b
# >>=	Performs Bitwise right shift on operands and assign value to left operand , a>>=b ,a=a>>b
# <<=	Performs Bitwise left shift on operands and assign value to left operand	a <<= b , a= a << b

#6. Special operators: There are some special type of operators like-
# Identity operators-
# 'is' and 'is not' are the identity operators both are used to check
# if two values are located on the same part of the memory.
# Two variables that are equal does not imply that they are identical.

#7. Membership operators-
# in and not in are the membership operators;
# used to test whether a value or variable is in a sequence.
# 'in True if value is found in the sequence
# not in True if value is not found in the sequence


print('shruti misra')
if 5 > 2:
    print("Five is greater than two!")
print("Five is greater than two!")