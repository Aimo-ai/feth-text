import csv

total = 0
progress = 0

with open("bundle.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if row[3] != "":
            progress += 1
        total += 1
    print(f"Переведено {progress} из {total} строк ({round(progress / total * 100)}%).")
