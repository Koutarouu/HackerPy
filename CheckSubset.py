for _ in range(int(input())):
	n,setA=int(input()),set(map(int,input().split()))
	n,setB=int(input()),set(map(int,input().split()))
	print(True if (setA-setB)==set() else False)
	print(not bool(setA.difference(setB)))
		