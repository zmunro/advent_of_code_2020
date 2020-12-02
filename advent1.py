from collections import defaultdict

num_dict = defaultdict(bool)
with open("files/advent1_and_2_file.txt") as advent1_and_2_f:
    for line in advent1_and_2_f.readlines():
        num_dict[int(line.strip())] = True

numbers = list(num_dict.keys())
for num in numbers:
    value_needed = 2020 - num
    if num_dict[value_needed]:
        print(num * value_needed)
        break
