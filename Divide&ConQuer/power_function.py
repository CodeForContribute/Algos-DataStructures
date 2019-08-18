# Method1 : Time Complexity : O(n)
def power(x, y):
    if y == 0:
        return 1
    elif int(y % 2) == 0:
        return power(x, int(y / 2)) * power(x, int(y / 2))
    else:
        return x * power(x, int(y / 2)) * power(x, int(y / 2))


# Method2: Time Complexity : O(log(n))

def power_function(x, y):
    if y == 0:
        return 1
    temp = power_function(x, int(y / 2))
    if y % 2 == 0:
        return temp * temp
    else:
        if y > 0:
            return x * temp * temp
        return (temp * temp) / x


if __name__ == '__main__':
    x = 2
    y = -3
    print(power(x, y))
    print('%.6f' % power_function(x, y))
