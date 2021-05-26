def recur(m):
    ll = len(m)
    if ll <= 1:
        return m
    mid = ll//2
    left = recur(m[:mid])
    right = recur(m[mid:])
    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i == len(left):
        res.extend(right[j:])
    if j == len(right):
        res.extend(left[i:])
    return res


L = [1, 20, 19, 18, 26, 5, 7, 8, 2, 3]
print("排序前：", L)
print("排序后：", recur(L))
print("稳定不")
