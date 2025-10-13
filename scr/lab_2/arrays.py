p=[]
def min_max(s):
    if s==p: return "ValueError"
    return min(s), max(s)
def unique_sorted(s):
    if s == p: return "ValueError"
    return list(set(sorted(s)))


def  flatten(s):
    if s == p: return "ValueError"
    v=[]
    for x in s:
        for i in x:
            if type(i) != int:
                return "TypeError"
            else:
                 v.append((i))
    return v


print("min_max")
print(min_max(s=[3, -1, 5, 5, 0]))
print(min_max(s=[42]))
print(min_max(s=[-5, -2, -9]))
print(min_max(s=[]))
print(" ")
print("unique_sorted")
print(unique_sorted(s=[3, 1, 2, 1, 3]))
print(unique_sorted(s=[]))
print(unique_sorted(s=[-1, -1, 0, 2, 2]))
print(unique_sorted(s=[1.0, 1, 2.5, 2.5, 0]))
print(" ")
print("flatten")
print(flatten(s=[[1, 2], [3, 4]]))
print(flatten(s=[[1, 2], (3, 4, 5)]))
print(flatten(s=[[1], [], [2, 3]]))
print(flatten(s=[[[1, 2], "ab"]]))