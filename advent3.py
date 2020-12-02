valid_passwords_count = 0
with open("advent3_and_4_file.txt") as advent3_f:
    for line in advent3_f.readlines():
        line_parts = line.split(" ")
        min_occurences = int(line_parts[0].split("-")[0])
        max_occurences = int(line_parts[0].split("-")[1])
        letter = line_parts[1].replace(":", "")
        password = line_parts[2]
        letter_count = password.count(letter)

        if letter_count >= min_occurences and letter_count <= max_occurences:
            valid_passwords_count += 1
print(valid_passwords_count)
