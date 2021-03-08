def discount_ten(param: list):
    discount = 0.9  # 0.9 --> 10% discount
    for i in range(len(param)):
        param[i] *= discount
    return param


prices = [2.45, 4.67, 1.20, 43.32]
print(str(discount_ten(prices)))
