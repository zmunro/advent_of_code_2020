import queue
from collections import defaultdict


lines = open("advent10.txt", 'r').readlines()
built_in_adapter_rating = max([int(x) for x in lines]) + 3

adapters = defaultdict(bool)
adapters.update({int(x): True for x in lines})

ways_to_reach_joltage = defaultdict(int)
ways_to_reach_joltage[0] = 1
joltages = queue.Queue()
joltages.put(0)

while not joltages.empty():
    joltage = joltages.get()
    if adapters[joltage + 1]:
        if ways_to_reach_joltage[joltage + 1] == 0:
            joltages.put(joltage + 1)
        ways_to_reach_joltage[joltage + 1] += ways_to_reach_joltage[joltage]
    if adapters[joltage + 2]:
        if ways_to_reach_joltage[joltage + 2] == 0:
            joltages.put(joltage + 2)
        ways_to_reach_joltage[joltage + 2] += ways_to_reach_joltage[joltage]
    if adapters[joltage + 3]:
        if ways_to_reach_joltage[joltage + 3] == 0:
            joltages.put(joltage + 3)
        ways_to_reach_joltage[joltage + 3] += ways_to_reach_joltage[joltage]

print(ways_to_reach_joltage[built_in_adapter_rating - 3])