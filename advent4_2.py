import re

passports_list = []
with open("files/advent4_input.txt", "r") as in_f:
    passport = {}
    for line in in_f.readlines():
        line = line.strip()
        if line == "":
            passports_list.append(passport)
            passport = {}
            continue
        for key_val in line.split(" "):
            passport[key_val.split(":")[0]] = key_val.split(":")[1]
    passports_list.append(passport)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
byr_pattern = re.compile("^((19[2-9][0-9])|(200[0-2]))$")

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
iyr_pattern = re.compile("^((201[0-9])|(2020))$")

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
eyr_pattern = re.compile("^((202[0-9])|(2030))$")

# hgt (Height) - a number followed by either cm or in:
hgt_pattern = re.compile("^((1[5-8][0-9]cm)|(19[0-3]cm)|(59in)|(6[0-9]in)|(7[0-6]in))$")

# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
hcl_pattern = re.compile("^(#[0-9,a-f]{6})$")

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
ecl_pattern = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$")

# pid (Passport ID) - a nine-digit number, including leading zeroes.
pid_pattern = re.compile("^([0-9]{9})$")

required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
valid_passports = 0
for passport_dict in passports_list:
    if not required_keys.issubset(set(passport_dict.keys())):
        continue
    if not byr_pattern.match(passport_dict['byr']):
        continue
    if not iyr_pattern.match(passport_dict['iyr']):
        continue
    if not eyr_pattern.match(passport_dict['eyr']):
        continue
    if not hgt_pattern.match(passport_dict['hgt']):
        continue
    if not hcl_pattern.match(passport_dict['hcl']):
        continue
    if not ecl_pattern.match(passport_dict['ecl']):
        continue
    if not pid_pattern.match(passport_dict['pid']):
        continue
    valid_passports += 1


print(f"valid_passports: {valid_passports}")