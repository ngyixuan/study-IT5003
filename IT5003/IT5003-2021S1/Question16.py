n, m = map(int, input().split())
target_language = input().split()
translator_dict = {}
for i in target_language + ["English"]:
    translator_dict[i] = {}

for _ in range(m):
    l1, l2, c = map(str, input().split())
    translator_dict[l1][l2] = int(c)  # cost
    translator_dict[l2][l1] = int(c) 


distance = {language: 1e9 for language in translator_dict.keys()}
cost = {language: 1e9 for language in translator_dict.keys()}
visited = {language: False for language in translator_dict.keys()}

queue = [('English',0,0)] #cost,step
distance['English'] = 0
cost['English'] = 0
visited['English'] = True

while(queue):
    current_lang, current_cost, current_step=queue.pop(0)
    for next_lang, next_cost in translator_dict[current_lang].items():
        new_step = current_step+1
        if(not visited[next_lang] and new_step<distance[next_lang]):
            distance[next_lang] = new_step
            cost[next_lang] = next_cost
            visited[next_lang]  = True
            queue.append((next_lang, next_cost, new_step))

total_cost = 0
impossible = False
for lang in target_language:
    if(lang==1e9):
        impossible = True
        break
    else:
        total_cost+=cost[lang]

print(total_cost if not impossible else print("Impossible"))




"""
4 6
Chinese French Portuguese Swedish
English Chinese 1
English French 1
English Portuguese 5
Chinese Portuguese 1
Portuguese Swedish 5
French Swedish 1

2 2
A B
English B 1
B A 2

"""
