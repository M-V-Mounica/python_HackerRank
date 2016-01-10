l = []
for i in range(0,int(raw_input())):
	a = raw_input().strip().split(" ")
	if a[0]=="insert":
		l.insert(int(a[1]),int(a[2]))
	if a[0]=="append":
		l.append(int(a[1]))
	if a[0]=="remove":
		l.remove(int(a[1]))
	if a[0]=="sort":
		l.sort()
	if a[0]=="pop":
		l.pop()
	if a[0]=="print":
		print l
	if a[0]=="reverse":
		l.reverse()
