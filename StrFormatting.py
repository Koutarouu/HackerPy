def print_formatted(number):
  width = len("{0:b}".format(number))
  for i in range(1,number+1):
    binary=bin(i).split('b')
    octal=oct(i).split('o')
    hexade=hex(i).split('x')
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,str(octal[1]),str(hexade[1].upper()),str(binary[1]),width=width))


def print_formatted2(number):
  width = len("{0:b}".format(number))
  #print(width)
  for i in range(1,number+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b} ".format(i,width=width))

print_formatted(17)
print("="*30)
print_formatted2(10)