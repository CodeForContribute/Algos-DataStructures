from sys import maxsize


def second_repeated_word_in_seq(arr, n):
    hash_map = dict()
    first = second = -maxsize
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1

    for i in range(n):
        if hash_map[arr[i]] > first:
            second = first
            first = hash_map[arr[i]]
        elif second < hash_map[arr[i]] < first:
            second = hash_map[arr[i]]

    for key, value in enumerate(hash_map):
        if hash_map[value] == second:
            return [value]
            # print value, end=" "


if __name__ == '__main__':
    arr = ["geeks", "for", "geeks", "for", "geeks", "aaa"]
    n = len(arr)
    a = second_repeated_word_in_seq(arr, n)
    print(a)
