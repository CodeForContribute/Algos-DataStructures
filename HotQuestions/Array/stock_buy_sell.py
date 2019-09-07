def stock_buy_sell(arr, n):
    init = 0
    res = []
    for j in range(1, n):
        if arr[j] < arr[j-1]:
            if j-1-init > 0:
                res.append((init, j-1))
            init = j
    if j - init > 0:
        res.append((init,j))
    if len(res) == 0:
        print("No Profit")
    else:
        print(res)

if __name__ == '__main__':
    arr = [100, 180, 260, 310, 40, 535, 695]
    stock_buy_sell(arr, len(arr))
