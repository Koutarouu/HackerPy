from collections import OrderedDict

N=int(input())
ordered_dictionary = OrderedDict()
for _ in range(N):
  #item, quantity = input().rsplit(None, 1)
  item,space,net_price=input().rpartition(' ')
  ordered_dictionary[item]=ordered_dictionary.get(item, 0)+int(net_price)
for k,v in ordered_dictionary.items():
  print(k,v)
print(ordered_dictionary,list(ordered_dictionary.items()))
"""
items=list(ordered_dictionary.items())
#items.sort()
for item in items:
    print(item[0],item[1])

Returns the value for key in the dictionary; if not found returns a default value.

Syntax
dict. get(key[, default])

key
Required. A key in the dictionary.
default
Optional. Value that is returned when the key is not found. Defaults to None, so that this method never raises a KeyError.
Return Value
The value of the key.
"""