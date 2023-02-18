"""
CSVファイルのパース
関数
csv.reader(f)
処理と戻り値
指定したCSVファイルをパースし、列要素が格納されたリストの行ごとのイテレータを返す
※fはファイルオブジェクトを指す

csv.readerの引数にファイルオブジェクトを指定すると、readerという列要素が格納されたリストの行ごとのイテレータを得ることができる

CSVファイルを扱う際、処理系によっては不要な改行コードが付加される場合があるため、open時にnewline=''を指定するようにする
"""


import csv

with open('sample.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダの読み飛ばし
    for row in reader:
        print(row)
