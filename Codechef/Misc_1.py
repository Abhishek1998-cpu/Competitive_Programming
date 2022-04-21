# Check the number is even or odd without using Modulo(%) operator

n = int(input())
# & convert its operand into boolean value and then compare it
if n & 1 == 0:
    print('EVEN')
else:
    print('ODD')
