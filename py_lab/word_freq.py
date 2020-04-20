#!/usr/bin/python3
import sys
import re

temp=0
ary=[]

num = int(sys.argv[2])
with open(sys.argv[1]) as f:
	for line in f.readlines():
		word = re.findall(r"[\w']+",line) 
		for i in word:
			ary.append(i)

dic = {}
for i in ary:
	count=0
	for k in ary:
		if i.lower()==k.lower():
			count+=1
	dic[i.lower()]=count
wordlist=sorted(dic.items(),reverse=True,key=lambda item: item[1])
for key, value  in wordlist:
	temp+=1
	if temp<=num:
		left='{:<30}'.format(key)
		print(left,value)
