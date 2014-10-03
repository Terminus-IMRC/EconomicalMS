#!/usr/bin/env python3
import math

def read_next_ms():
	try:
		s=input()
	except EOFError:
		return None
	s=s.split()
	return [int(i) for i in s]

def EconomicalMS():
	cur_min_length=float("inf")
	cur_most_economical_ms=None

	s=read_next_ms()

	Ceilings=len(s)
	X=math.sqrt(Ceilings)

	if math.floor(X)!=math.ceil(X):
		print("error: line length is not a numerical square")
		exit(1)

	X=int(X)

	#print("X:", X)
	#print("Ceilings:", Ceilings)

	ms_xhash=[None for i in range(Ceilings)]
	ms_yhash=[None for i in range(Ceilings)]
	
	while s!=None:
		for i in range(Ceilings):
			ms_xhash[s[i]-1]=i%X
			ms_yhash[s[i]-1]=int(i/X)
		length=0
		for i in range(Ceilings-1):
			length+=math.sqrt((ms_xhash[i+1]-ms_xhash[i])**2+(ms_yhash[i+1]-ms_yhash[i])**2)
		if length<cur_min_length:
			cur_min_length=length
			cur_most_economical_ms=s
		s=read_next_ms()

	print("The most economical MS:", end="")
	for i in range(Ceilings):
		print(" ", cur_most_economical_ms[i], sep="", end="")
	print()
	print("The length:", cur_min_length)

def mine():
	EconomicalMS()

if __name__=='__main__':
	mine()
