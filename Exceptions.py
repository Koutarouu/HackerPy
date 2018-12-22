t=int(input())

while t>0:
  try:
    a,b=map(int,input().strip().split())
    print(a//b)
  except (ValueError,ZeroDivisionError) as e:
    print("Error Code:",e)
  finally:
    t-=1
