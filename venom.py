class Snake:
	def __init__(self,name,length,venom):
		self.name=name
		self.length=length
		self.venom=venom
	def print(self):
		print(self.name)
l=[]
def snake(name,length,venom):
	A=Snake(name,length,venom)
	l.append(A)
def findByVenom(v):
	for s in l:
		if s.venom==v:
			s.print()
def findByLength(d):
	for s in l:
		if s.length==d:
			s.print()

with open("snakes.txt", "r") as f:
	s=f.readlines()
	n=int(s[0])
	for i in range(n):
		string=s[i+1]
		string=string.split(" ")
		name, length, venom = string[0], int(string[1]), int(string[2])
		snake(name,length,venom)
	n1=int(s[n+1])
	for i in range(n+2,n+2+n1):
		string=s[i]
		string=string.split(" ")
		command, val= string[0], int(string[1])
		if command=='V'	:
			findByVenom(val)
		elif command=='L' :
			findByLength(val)
		else :
			print("Invalid")

	
	
	



