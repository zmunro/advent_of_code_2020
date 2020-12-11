valid_passwords_count = 0
with open("files/advent2_input.txt") as advent3_f:
    for line in advent3_f.readlines():
        line_parts = line.split(" ")
        first_index = int(line_parts[0].split("-")[0]) - 1
        second_index = int(line_parts[0].split("-")[1]) - 1
        letter = line_parts[1].replace(":", "")
        password = line_parts[2]
        if (password[first_index] == letter) != (password[second_index] == letter):
            valid_passwords_count += 1
print(valid_passwords_count)
