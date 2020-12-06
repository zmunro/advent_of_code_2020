# Code Golf
seat_ids = [int(l.translate({76:48,70:48,66:49,82:49}),2) for l in open("5.txt","r")]
print(max(list(set(range(max(seat_ids))) - set(seat_ids))))