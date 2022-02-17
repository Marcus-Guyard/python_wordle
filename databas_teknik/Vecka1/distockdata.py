import csv

volume = {}
change_percent = {}
aktie_count = {}
aktie_count_2 = {}

with open('di_stock_data.csv', newline="") as f:
    reader = csv.DictReader(f)

    for line in reader:
        volume[line["name"]] = float(line["volume"])
        change_percent[line["name"]] = float(line["change_percent"])

        aktie_count[line["list"]] = aktie_count.get(line["list"], 0) + int(line["volume"])
        aktie_count_2[line["list"]] = aktie_count_2.get(line["list"], 0) + 1


print(f"Störst volym --> {max(volume, key=volume.get)}, {max(volume.values())}")
print(f"Minst volym --> {min(volume, key=volume.get)}, {min(volume.values())}\n")

print(f"Steg mest --> {max(change_percent, key=change_percent.get)} {max(change_percent.values())}%")
print(f"Sjönk mest --> {min(change_percent, key=change_percent.get)} {min(change_percent.values())}%\n")

print("Hur många av respektiv aktie!")
for val, key in aktie_count.items():
    print(f"{val} --> {key} stycken aktier")

print()
print("Antalet Olika aktier")
for val, key in aktie_count_2.items():
    print(f"{val} --> {key} stycken aktier")
