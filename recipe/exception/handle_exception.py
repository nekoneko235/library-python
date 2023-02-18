def div_num(a, b):
    try:
        val = a/b
        print(val)
    except ZeroDivisionError:
        print("Zero Division Error")


div_num(8, 2)
div_num(7, 0)
div_num(5, 2)
