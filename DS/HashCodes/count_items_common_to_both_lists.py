def count_items(list1, list2):
    count = 0
    for item1 in list1:
        for item2 in list2:
            if item1[0] == item2[0] and item1[1] != item2[1]:
                count += 1
    return count


def count_items_hashing(list1, list2):
    count = 0
    hash_map = dict()
    for item in list1:
        if item[0] not in hash_map.keys():
            hash_map[item[0]] = item[1]
    for item2 in list2:
        if item2[0] in hash_map.keys():
            if item2[1] != hash_map[item2[0]]:
                count += 1
    return count


if __name__ == '__main__':
    list1 = [("apple", 60), ("bread", 20),
             ("wheat", 50), ("oil", 30)]
    list2 = [("milk", 20), ("bread", 15),
             ("wheat", 40), ("apple", 60)]

    print("Count = ", count_items(list1, list2))
    print("Count = ", count_items_hashing(list1, list2))

