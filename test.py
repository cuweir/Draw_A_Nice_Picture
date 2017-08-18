try:
    f = open('C:/Users/C.U.Weir/Documents/GitHub/Draw_A_Nice_Picture/test.txt', 'w')
    f.truncate()
finally:
    if f:
        f.close()