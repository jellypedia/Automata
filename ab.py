#starts with ab
table = [
    [0,1,3],
    [1,3,2],
    [2,2,2],
    [3,3,3]
]
# print(transitionTable[0][1])
state = 0

strInput = input("Enter string: ")

for ch in strInput:
    if state == 2 or state == 3:
        break
    if ch == 'a':
        state = table[state][1]
    if ch == 'b':
        state = table[state][2]

if state == 2:
    print("Accepted string")
if state == 3:
    print("Rejected string")


