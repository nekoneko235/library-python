"""
CSVファイルへの書き出し
関数
csv.writer(f, lineterminator='改行コード')
戻り値
リストの内容をCSV形式で書き込むことができるwriterオブジェクト
※ fはファイルオブジェクトを指す

csv.writerの引数にファイルオブジェクトと改行コードを指定すると、リストの内容をCSV形式で書き込むことができるwriterというオブジェクトを得ることができる

また、読み込みのときと同様の理由でCSVファイルを扱う際は、open時にnewline=''を指定するようにする
"""

import csv

sample_list = [["col1", "col2", "col3"],
               [101, 102, 103],
               [201, 202, 203],
               [301, 302, 303]]

with open('sample2.csv', 'w', newline='') as f:
    writer = csv.writer(f, lineterminator='\n')
    for row in sample_list:
        writer.writerow(row)
