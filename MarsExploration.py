#!/bin/python

import sys
S = raw_input().strip()
messageLength = len(S)
rep = messageLength / 3
trueMessage = 'SOS'*rep

count = 0
for i in range(messageLength):
    if S[i] != trueMessage[i]:
        count += 1
print count
