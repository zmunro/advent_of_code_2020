from collections import defaultdict

seat_ids = defaultdict(bool)
with open("files/advent5_input.txt", "r") as in_f:
    for line in in_f.readlines():
        seat_row = int(line.strip()[:7].replace("F","0").replace("B", "1"), 2)
        seat_col = int(line.strip()[-3:].replace("L","0").replace("R", "1"), 2)
        seat_ids[seat_row * 8 + seat_col] = True

for id_key in list(seat_ids.keys()):
    if not seat_ids[id_key + 1] and seat_ids[id_key + 2]:
        print(id_key + 1)