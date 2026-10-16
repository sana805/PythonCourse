# Python Operators - All in One Program

a = 10
b = 3

# 1. Arithmetic Operators
print("ARITHMETIC OPERATORS")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)
print("Floor Division:", a // b)

# ARITHMETIC OPERATORS
# Addition: 13
# Subtraction: 7
# Multiplication: 30
# Division: 3.3333333333333335
# Modulus: 1
# Power: 1000
# Floor Division: 3


# 2. Comparison Operators
print("\nCOMPARISON OPERATORS")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)



# COMPARISON OPERATORS
# Equal: False
# Not Equal: True
# Greater than: True
# Less than: False
# Greater or Equal: True
# Less or Equal: False

# 3. Assignment Operators
print("\nASSIGNMENT OPERATORS")
x = 10
print("x =", x)

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 4
print("x /= 4:", x)


# 4. Logical Operators
print("\nLOGICAL OPERATORS")
age = 25

print("AND:", age > 18 and age < 30)
print("OR:", age < 18 or age > 30)
print("NOT:", not(age > 18))


# 5. Membership Operators
print("\nMEMBERSHIP OPERATORS")
names = ["Sana", "Ali", "John"]

print("Sana in names:", "Sana" in names)
print("Rahul not in names:", "Rahul" not in names)


# 6. Identity Operators
print("\nIDENTITY OPERATORS")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)


# 7. Bitwise Operators
print("\nBITWISE OPERATORS")
p = 5
q = 3

print("AND:", p & q)  # containing 1->1=1 otherwise 0
print("OR:", p | q)  #containing  if statement has 1 create 1 otherwise 0
print("XOR:", p ^ q) # differnt ->1 , same->0
print("NOT:", ~p)   # ~(5+1)= -6
print("Left Shift:", p << 1)   # 5*2 if left num 1  # 5*4 if left num is 2
print("Right Shift:", p >> 3)  # 5%2 if r num is 1 # 5%4 if r num is 2