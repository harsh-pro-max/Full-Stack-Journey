# 1.Write a python script to print any number and its binary equivalent.
x=564
binary=bin(x)
print(binary)

# 2. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
x=0b1100101
print(int(x))

# 3. Write a python script to store a hexadecima number 2F in a variable and print it in octal format.
x=0x2f
print(oct(x))

# 4.Write a python script to store an octal number 125 in a variable and print it in binary format.
x=0o125
print(bin(x))

# 5. Write a python script to add two numbers 25(in octal) and 39 (in hexadecimal) and display the result in binary format.

add=0o25+0x39
print(bin(add))