able File  11 lines (11 sloc)  250 Bytes

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            index += 1
        except:
            break
    print()
    return(index)