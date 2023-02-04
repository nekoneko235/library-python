# break が実行されなかったときのみ else 以下の処理を実行
l = [0, 3, 1, 10]
for x in l:
    if x < 0:
        print("負の数を検知しました")
        break
else:
    print("負の数は見つかりませんでした")
