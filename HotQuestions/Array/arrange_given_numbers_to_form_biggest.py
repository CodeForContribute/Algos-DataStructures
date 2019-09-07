from itertools import permutations
"""
map() function returns a list of the results after applying the given function to each item of a given iterable 
      (list, tuple etc.)
Syntax :map(fun, iter)
"""
def largest(arr, n):
    lst = []
    for i in permutations(arr, n):
        lst.append("".join(map(str, i)))
    return max(lst)

if __name__ == '__main__':
    a = [54, 546, 548, 60, ]
    print(largest(arr=a, n=len(a)))