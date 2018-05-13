def chop(t):
    del t[0]
    del t[-1]
    return None


def middle(t):
    return t[0:5]


t = [1, 2, 3, 4, 5]
newt = middle(t)
print(newt)
chop(t)
print(t)
