s = raw_input()
n = raw_input().split(" ")
k = int(n[0])
print s[:k]+n[1]+s[k+1:]
