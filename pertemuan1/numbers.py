#Python Numbers
x = 11    # int
y = 3.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#Int
x = 100
y = 25071206988
z = -99999

print(type(x))
print(type(y))
print(type(z))

#Float
x = 3.80
y = 4.0
z = -40.10

print(type(x))
print(type(y))
print(type(z))

x = 21e4
y = 42E4
z = -91.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex
x = 3+2j
y = 4j
z = -4j

print(type(x))
print(type(y))
print(type(z))

#Type Conversion
#convert dari int ke float:
x = float(4)

#convert dari float ke int:
y = int(3.8)

#convert dari int ke complex:
z = complex(4)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#Angka Acak
import random

print(random.randrange(1, 11))
