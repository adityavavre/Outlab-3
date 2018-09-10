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
def find_total(x1,y1,x2,y2):
	def line_eq(x,y):
		if ((x-x1)*(y2-y1)-(y-y1)*(x2-x1)) == 0 :
			return True
		return False
	count=0
	for i in location_list :
		if line_eq(i['x'],i['y']) :
			count=count+1
	print(count)
s=input()
s=s.split(" ")
x1, y1, x2, y2 = int(s[0]), int(s[1]), int(s[2]), int(s[3])
find_total(x1,y1,x2,y2)


