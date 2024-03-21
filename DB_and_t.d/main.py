import pymorphy3

input_file = open("DB_v0.2.txt", "r", encoding="utf-8")
data = input_file.readlines()
input_file.close()
output_file = open("DB_v0.5.txt", "wt", encoding='utf-8')
s = 1
for line in data:
    if s % 2 != 0:
        output_file.write(line)
    s += 1
output_file.close()
