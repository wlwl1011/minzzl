#!/usr/bin/python3
def change(value):
	b=0
	inputa=str(value)
	b=int(inputa,2)
	o=format(b,'o')
	h=format(b,'x')
	print("OCT>",o)
	print("DEC>",b)
	print("HEX> %X" % (b))
