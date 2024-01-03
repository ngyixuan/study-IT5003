
candidate = list(map(int,input().split()))
final_candidate = []
maxValue = max(candidate)
count = candidate.count(maxValue)
for i in range(count):
    final_candidate.append(candidate.pop(candidate.index(maxValue))) 
print(final_candidate)

    
# 8 1 2 3 5 6 7