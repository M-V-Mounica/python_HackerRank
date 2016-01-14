raw_input()
l=map(int, raw_input().strip().split(" "))
print sorted(list(set(l)))[-2]
