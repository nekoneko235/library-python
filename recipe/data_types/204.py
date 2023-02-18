import csv

with open('sample.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダの読み飛ばし
    for row in reader:
        print(row)
