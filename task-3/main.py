def add_hello(parm: list):  # : list notates the data type
    parm.append("hello")
    return parm


random_words = ["list", "of", "word", "random"]
print(add_hello(random_words))
