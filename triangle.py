
s=input("Enter first coordinate : ")
s=s.split(" ")
x1, y1 = float(s[0]), float(s[1])
s=input("Enter second coordinate : ")
s=s.split(" ")
x2, y2 = float(s[0]), float(s[1])
s=input("Enter third coordinate : ")
s=s.split(" ")
x3, y3 = float(s[0]), float(s[1])
s=input("Enter coordinates of the key : ")
s=s.split(" ")
x, y = float(s[0]), float(s[1])

def area(x1, y1, x2, y2, x3, y3):
	return (1/2)*abs((x1*(y3-y2)+x2*(y1-y3)+x3*(y2-y1)))
def insideOut():
	if area(x1, y1, x2, y2, x, y)+area(x2, y2, x3, y3, x, y)+area(x3, y3, x1, y1, x, y)==area(x1, y1, x2, y2, x3, y3):
		print("INSIDE")
	else:
	    print("OUTSIDE")	
insideOut()	    

