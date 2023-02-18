"""
スクリプトの実行時に指定されたコマンドライン引数を使用する場合、
sysモジュールのargvを利用する。argvはリスト型で、実行時に指定されたコマンドライン引数が文字列として格納される
ただしリストの0番目にはスクリプト名が格納される
"""


from sys import argv


if 3 <= len(argv):
    print(argv[0])
    print(argv[1])
    print(argv[2])
else:
    print("引数を3つ指定してください。")
