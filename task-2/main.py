def bubble_sort(args):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(args) - 1):
            if args[i] > args[i + 1]:
                args[i], args[i + 1] = args[i + 1], args[i]
                swapped = True
    return args


print(bubble_sort([3, 8, 3, 2, 5, 7, 1, 6, 8, 2]))
