# Write a Python script to print any number and its binary equivalent.
a=101
print("Number %d to binary"%(a),bin(a))

# Write a Python script to store binary number 1100101 in a variable and print it in decimal format.
binary=0b1100101
dec=int(binary)
print(dec)

#Write a Python script to store hexadecimal number 2F in a variable and print it in octal format.

hexa=0x2f
print(oct(hexa))

# Write a Python script to store octal number 125 in a variable and print it in binary format.
o=0o125
print(bin(o))

# Write a Python script to add two numbers: 25 (in octal) and 39 (in hexadecimal), and display the result in binary format.
num=0o25
num2=0x39
print(bin(num+num2))

