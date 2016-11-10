n = raw_input()
arr = raw_input().strip().split(' ')
myset = list(set(arr))
countElement = []

for i in range(len(myset)):
    countElement.append(arr.count(myset[i]))

print sum(countElement) - max(countElement)
