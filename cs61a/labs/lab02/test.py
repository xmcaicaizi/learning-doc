def square(x):
    return x*x

def Addone(x):
    return x+1


def composite(f,g):

    return lambda x: g(f(x)) == f(g(x))

a = composite(square, Addone)
