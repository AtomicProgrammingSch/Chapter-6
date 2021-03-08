bank_holidays_in_month = [1, 0, 1, 1, 2, 0, 0, 1, 0, 0, 0, 2]


def bank_holiday(month):
    month -= 1  # index position includes 0
    return bank_holidays_in_month[month]


print("Number of bank holidays: " + str(bank_holiday(5)))  # 5th month --> may
