'''
n=number of target language, m = number of translator
use a dictionary to store the adjacency list for each language in your graph, each key is the target language, 
and the value is the translator language and cost in term of dictionary

'''
n,m  = map(int,input().split())
target_language = input().split()
translator_dict = {}
for i in target_language+['English']:
    translator_dict[i] = {}

for _ in range(m):
    l1,l2,c = map(str, input().split())
    translator_dict[l1] [l2] = int(c)
    translator_dict[l2] [l1] = int(c)

print(translator_dict)


