def smartdiv(function):
    def inner(*args):
        if args[1]==0:
            return
        return function(*args)

    return inner

@smartdiv
def div(a,b):
    print(a/b)


div(5,0)
