import random
import string


def random_generator(n):
    pass


def random_number_generator(n, arr):
    # 1<=a<=10^9の範囲でランダムな数を生成する
    for _ in range(n):
        arr.append(random.randint(1, 10**9))


def random_character_generator(n, arr):
    # a-zのランダムな文字を生成する
    for _ in range(n):
        arr.append(random.choice(string.ascii_lowercase))


def random_string_generator(n, arr):
    # a-zの5文字のランダムな文字列を生成する
    for _ in range(n):
        arr.append("".join(random.choice(string.ascii_lowercase) for _ in range(5)))


def solver_expected(n):
    # 愚直解法
    pass


def solver(n):
    # 解法
    pass


def main():
    count_wrong_answers = 0
    number_of_test_cases = 10
    for i in range(1, number_of_test_cases):
        # 標準入力をランダムに生成する
        n = random.randint(1, 10)
        # テストケースをsolver()とsolver_expected()に渡して出力結果を取得する
        j1 = solver(n)
        j2 = solver_expected(n)
        # 出力結果が異なる場合は、出力結果をtestcase.txtに追加で書き込みし保存する
        if j1 != j2:
            count_wrong_answers += 1
            with open("testcase.txt", "a") as f:
                f.write("WA on test case: " + str(i) + "\n")
                f.write("Expected: " + str(j2) + " Output: " + str(j1) + "\n")
                f.write(str(n) + "\n")
                # 配列の出力内容を確認したい場合は以下のコメントアウトを外す
                # for i in range(n):
                #     f.write(str(arr[i]) + " ")
                f.write("\n")
    if count_wrong_answers == 0:
        print("AC!")
    else:
        print("WA: " + str(count_wrong_answers))


if __name__ == "__main__":
    main()
