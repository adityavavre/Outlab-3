with open("employees.txt", "r") as f:
	#s=f.readlines()
	for i in f:
		h=i.split(" ")
		print(h[0][3:]+h[0][:3])