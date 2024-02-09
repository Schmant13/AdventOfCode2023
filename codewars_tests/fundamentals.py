def square_digits(num):
    cat = ""
    for n in str(num):
        sqr = int(n)**2
        nstr = str(sqr)
        print(nstr)
        cat + nstr
        print(sqr)
    return cat

print(square_digits(9119))