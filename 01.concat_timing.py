import timeit

def operatorConcat():
    return "a" + "b"

def joinConcat():
    return "".join(["a", "b"])

def percentConcat():
    return "%s%s" % ("a", "b")

def fStringConcat():
    return "{}{}".format("a", "b")


if __name__ == "__main__":
    print("plus operator:\t\t", timeit.timeit(operatorConcat, number=1000000))
    print("percent sign:\t\t", timeit.timeit(percentConcat))
    print("join method:\t\t", timeit.timeit(joinConcat))
    print("f-string:\t\t", timeit.timeit(fStringConcat))