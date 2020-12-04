

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

required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
valid_passports = 0
for passport_dict in passports_list:
    if required_keys.issubset(set(passport_dict.keys())):
        valid_passports += 1


print(f"valid_passports: {valid_passports}")