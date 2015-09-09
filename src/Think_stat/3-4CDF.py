def cdf(t,x):
    count = 0.0
    for value in t:
        if value <= x:
            count += 1.0
    prob =  count / len(t)
    return prob

t = [1,2,2,2,3,5]
print(cdf(t,2))