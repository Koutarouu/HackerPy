import textwrap
def wrap(string, max_width):
  print(textwrap.wrap(string,max_width))
  return textwrap.fill(string,max_width)

print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4))

#Divide el texto que le mandemos en la longitud maxima que le mandemos y si falta
#simplemente no lo acompleta