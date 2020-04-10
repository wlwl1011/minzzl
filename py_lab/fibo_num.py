#!/usr/bin/python3

n=int( input("fibonacci number?"))
a=0
b=1
temp=0

for i in range(0,n):
	temp=a
	a=b
	b=temp+a
	if(i!=(n-1)):
		print('%d,' % a,end='')
	else:
		print('%d' % a)
print("F%d = %d" % (n,a))
	 
