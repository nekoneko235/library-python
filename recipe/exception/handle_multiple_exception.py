def div_num(a, b):
    try:
        val = a/b
        print(val)
    except TypeError:
        print("Type Error")
    except ZeroDivisionError:
        print("Zero Division Error")
    except Exception:
        print("Exception")


div_num("abcdefg", 2)
div_num(7, 0)
