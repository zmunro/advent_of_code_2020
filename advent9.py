nums = [int(l.strip()) for l in open('9.txt', 'r').readlines()]

def do_nums_sum(nums_to_sum, num):
    nums_to_sum.sort()
    l_index, r_index = 0, 24
    while l_index != r_index:
        if nums_to_sum[l_index] + nums_to_sum[r_index] > num:
            r_index -= 1
        elif nums_to_sum[l_index] + nums_to_sum[r_index] < num:
            l_index += 1
        else:
            return True
    return False

for index in range(25, len(nums)):
    nums_to_sum = nums[index - 25 : index]
    if not do_nums_sum(nums_to_sum, nums[index]):
        answer = nums[index]
        print(f"Part 1: {answer}")
        break

l_index, r_index = 0, 1
while True:
    if sum(nums[l_index: r_index + 1])< answer:
        r_index += 1
    elif sum(nums[l_index: r_index + 1]) > answer:
        l_index += 1
    else:
        print(f"Part 2: {min(nums[l_index: r_index + 1]) + max(nums[l_index: r_index + 1])}")
        break

