adapters = [int(x.strip()) for x in open("10.txt", 'r').readlines()] + [0]
adapters.sort()
adapters.append(adapters[-1] + 3)
ones = 0
total = 1
permutations = [1, 1, 2, 4, 7, 12]
for index, adapter in enumerate(adapters[1:], 1):
    delta = adapter - adapters[index - 1]
    if delta == 3:
        total *= permutations[ones]
        ones = 0
    else:
        ones += 1

print(total)
