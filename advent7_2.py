from collections import defaultdict
all_bag_descs = defaultdict(list)
for line in [x for x in open("7.txt", 'r').readlines() if "no other" not in x]:
    all_bag_descs[line.split('bags')[0].strip()] = [(' ' .join(x.split(' ')[2:4]), int(x.split(' ')[1])) for x in line.split('contain')[1].split(',')]

found_bags_dict = defaultdict(bool)
found_bags_dict.update({"shiny gold": True})
search_for_bags_list = ["shiny gold"]
index = 0
total_bags = 0


def get_bags(bag_info):
    return  bag_info[1] + bag_info[1] * sum([get_bags(x) for x in all_bag_descs[bag_info[0]]])

print(get_bags(('shiny gold', 1)) - 1)