from collections import defaultdict
all_bag_descs = defaultdict(list)
relationship_bags = defaultdict(set)
for line in open("7.txt", 'r').readlines():
    all_bag_descs[line.split('bags')[0].strip()] = [' ' .join(x.split(' ')[2:4]) for x in line.split('contain')[1].split(',')]
    for bag in all_bag_descs[line.split('bags')[0].strip()]:
        relationship_bags[bag].add(line.split('bags')[0].strip())

found_bags_dict = defaultdict(bool)
found_bags_dict.update({"shiny gold": True})
search_for_bags_list = ["shiny gold"]
index = 0
while True:
    if index == len(search_for_bags_list):
        break
    added_bags = [x for x in relationship_bags[search_for_bags_list[index]] if not found_bags_dict[x]]
    search_for_bags_list += added_bags
    found_bags_dict.update({x: True for x in added_bags})
    index += 1

print(len(search_for_bags_list) - 1)
