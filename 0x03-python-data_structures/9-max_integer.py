def max_integer(my_list=[]):
    if not my_list:
        return None

    max_int = my_list[0]
    for nuh in my_list:
        if nuh > max_int:
            max_int = nuh

    return max_int
