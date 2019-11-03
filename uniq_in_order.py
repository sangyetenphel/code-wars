def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    uniq_list = [iterable[0]]
    for i in range(len(iterable) - 1):
        if iterable[i+1] == iterable[i]:
            pass
        else:
            uniq_list.append(iterable[i+1])
    return uniq_list

iterable = ()
print(unique_in_order(iterable))
