marksheet = []
l=[]
for i in range(0,int(input())):
	l1=[]
	name = raw_input()
	mark = float(raw_input())
	l1.append(name)
	l1.append(mark)
	marksheet.append(l1)
m= sorted(list(set([marks for name, marks in marksheet])))[1]
for i in marksheet:
	if m==i[1]:
		l.append(i[0])
l.sort()
for i in l:
	print i
