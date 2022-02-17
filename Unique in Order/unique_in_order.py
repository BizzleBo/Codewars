def unique_in_order(iterable):
    list = []
    for item in range(len(iterable)):
        if item == 0 or iterable[item] != iterable[item-1]:
            list.append(iterable[item])
    return list