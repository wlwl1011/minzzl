#!/usr/bin/python3
from my_pkg.binary_to_other import *
from my_pkg.union_intersection import *
import re
while True:
	n= input("Select menu: 1)conversion 2)union/intersection 3)exit?")
	num=int(n)
	if num==1:
		value = input("input binary number:" )
		change(value) 
	elif num==2:
		first=input("1st list:")
		second=input("2nd list:")
		f=re.findall(r"[\d']+",first)
		s=re.findall(r"[\d']+",second)
		ff=list(map(int,f))
		ss=list(map(int,s))
		uniona(ff,ss)	
		intersectiona(ff,ss)
	elif num==3:
		break;
