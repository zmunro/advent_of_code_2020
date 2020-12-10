from collections import defaultdict
lines = open("advent10.txt", 'r').readlines()
built_in_adapter_rating = max([int(x) for x in lines]) + 3
adapters = [0] + [int(x) for x in lines] + [built_in_adapter_rating]
adapters.sort()
uses = [0,0,0]
for index in range(1,len(adapters)):
    uses[adapters[index] - adapters[index - 1] - 1] += 1
print(uses)