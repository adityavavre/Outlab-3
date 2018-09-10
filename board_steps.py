location_list=[]
with open("students.txt","r") as f:
    s=f.readlines()
    n=int(s[0])
    for i in range(n):
        string=s[i+1]
        string=string.split(" ")
        x=int(string[0])
        y=int(string[1])
        location_list.append({"x":x, "y":y})
def find_loc(x1,y1,x2,y2):
	if x1>x2 or y1>y2 :
		print('-1')
	else :
		steps=(x2-x1)+(y2-y1)
		print(steps)
	
s=input()
s=s.split(" ")
x1, y1, x2, y2 = int(s[0]), int(s[1]), int(s[2]), int(s[3])
find_loc(x1,y1,x2,y2)
