def add_hello(param: list):  # : list notates the data type
    param.append("hello")
    return param


random_words = ["list", "of", "word", "random"]
print(add_hello(random_words))
