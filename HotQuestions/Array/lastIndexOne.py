def lastIndex(string, n):
    for j in range(n-1,-1, -1):
        if string[j] == '1':
            return j
    return -1

if __name__ == '__main__':
    string = '000000001'
    n = len(string)
    print(lastIndex(string, n))
