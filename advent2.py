from collections import defaultdict


def get_nums_that_sum(number_list, desired_sum):
    num_dict = defaultdict(bool)
    num_dict.update({x: True for x in number_list})
    for num in number_list:
        value_needed = desired_sum - num
        if num_dict[value_needed]:
            return num * value_needed
    return 0


numbers = []
with open("files/advent1_and_2_file.txt") as advent1_and_2_f:
    for line in advent1_and_2_f.readlines():
        numbers.append(int(line.strip()))


for index in range(len(numbers)):
    ans = get_nums_that_sum(numbers[index:], 2020 - numbers[index])
    if ans != 0:
        print(ans * numbers[index])
        break
