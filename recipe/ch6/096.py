def div_num(a, b):
    try:
        val = a/b
        print("Result:{}".format(val))
    except:
        print("Exception handling")
    else:
        print("Process completed successfully")
    finally:
        print("Process terminated")


print("----- Successfully -----")
div_num(4, 2)
print("----- Exception -----")
div_num(10, 0)
