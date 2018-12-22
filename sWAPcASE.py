def swap_case(s):
  newW=""
  for i in s:
    if i.lower()!=i:
      i=i.lower()
      newW+=i
    else:
      i=i.upper()
      newW+=i
  return newW

print(swap_case("HackerRank.com presents 'Pythonist 2'"))