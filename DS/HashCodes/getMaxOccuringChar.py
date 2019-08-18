def get_max_occur_elements(str):
    hash_map = dict()
    for i in str:
        if i in hash_map.keys():
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    maximum = -1
    ch = None
    max_occurring_list = list()
    for key, value in hash_map.items():
        if value > maximum:
            max_occurring_list.append(key)
    print(max_occurring_list[2])


if __name__ == '__main__':
    string = "cbbbaaaabccc"
    (get_max_occur_elements(string))
