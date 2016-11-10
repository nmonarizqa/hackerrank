n = raw_input()
for i in range(int(n)):
    word = raw_input()
    comparison = []
    for j in range(len(word)-1):
        forward = ord(word[j+1]) - ord(word[j])
        ix = len(word) - j
        backward = ord(word[ix-2]) - ord(word[ix-1])
        comp = abs(forward) - abs(backward)
        if comp == 0:
            comparison.append(comp)
        else:
            print "Not Funny"
            break
    if len(comparison) == len(word)-1:
        print "Funny"
