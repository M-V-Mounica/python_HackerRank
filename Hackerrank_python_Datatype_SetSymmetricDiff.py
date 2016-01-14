raw_input()
s1 = set(map(int, raw_input().strip().split(" ")))
raw_input()
s2 = set(map(int, raw_input().strip().split(" ")))
for i in sorted(s1^s2):
	print i
