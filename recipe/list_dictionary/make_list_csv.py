# 文字列要素だけのリストをCSV文字列に変換する
lst = ["Apple", "Orange", "Banana"]
csv_str = ",".join(lst)
print(csv_str)

# 文字列以外を含むリストをCSV文字列に変換する
lst = ["Apple", "Orange", 200]
csv_str = "\t".join(map(str, lst))
print(csv_str)
