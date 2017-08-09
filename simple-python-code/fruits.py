s,t = input().strip().split()
s,t = [int(s),int(t)]
a,b = input().strip().split()
a,b = [int(a),int(b)]
m,n = input().strip().split()
m,n = [int(m),int(n)]
apple = [int(fruit) for fruit in input().strip().split()]
orange = [int(fruito) for fruito in input().strip().split()]
count = 0
for i in apple:
	if(s <= (i+a) and (i+a) <= t):
		count = count+1
print(count)
count = 0
for i in orange:
	if(s <= (i+b) and (i+b) <= t):
		count = count + 1
print(count)
	
