from collections import deque
for i in range(int(input())):
    n = int(input())
    sideLengths = deque(map(int, input().strip().split()))
    notPossible = 0
    top = 0
    biggerSide = 0
    while notPossible == 0:
        if len(sideLengths) == 0:
            break
        else:
            left = sideLengths[0]
            right = sideLengths[-1]
            if left >= right:
                biggerSide = left
                sideLengths.popleft()
            elif left < right:
                biggerSide = right
                sideLengths.pop()
            if top == 0 or biggerSide <= top:
                top = biggerSide
            elif biggerSide > top:
                notPossible = 1
                print("No")            
    if notPossible == 0:
        print("Yes")