
L = list(map(int, input().split())) # N distinct integers (+ve and -ve)
N = len(L)
K=3
found=False
result = []

L = sorted(L)
for i in range(N):
    current =i
    left = i+1
    right = N-1
    if(L[0]>0): break
    while(left<right):
        total = L[current]+L[left]+L[right]
        if(total<0):
            left+=1
        elif(total>0):
            right-=1
        else:
            found=True
            print( L[current],L[left],L[right])
            break



if not found:
    print("No such triple")

