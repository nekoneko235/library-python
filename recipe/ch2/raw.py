"""
raw文字列を使用すると、エスケープシーケンスを無効化できる

ただし、文字列を囲んだ引用符を文字列中で使用する場合については、
\マークでのエスケープが必要となる
また、このことが理由で文字列末尾に奇数個の\がある場合、
最後の\が閉じ引用符をエスケープしてしまうため、エラーとなる
回避策として末尾に\を連結するという手がある
"""
win_path1 = "c:\\work\\sample"
print(win_path1)
win_path2 = r"c:\work\sample"
print(win_path2)
text = r'Beginner\'s Guide'
win_path3 = r'C:\work' + '\\'
