#global
a=23
b=65


def production():
    #local
    a=23
    b=65
    print("Mul:",a*b)

production()
print("Sum:",a+b)