#implict type conversion
integer = 56
float = 22.14

# addition of integer and float
sum = integer + float

print(sum)

# the output will be in float as python converts integer to float while adding

# type() function
print("datatype of sum:" , type(sum))

# explicit type conversion
float = 55.2
# conversion to integer
integer = int(float)
print(integer , " , number type:", type(integer))

# conversion of string to float and integer
a = '96'
integer = int(a)

Float = float(a)
print("integer no. :", integer )
print("Float no.:" , Float)

# use '\n' for the end of a string
print('hello \n\n', 78)

# errors
a = '89.0'
b = int(a)
print(b)

float = 6.8
integer = int(float)

print(float)
print(integer) # python removes the decimal part