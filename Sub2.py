#l = [12345, 12, 4938338, 1, 3033213, 17]
#def f(l):
#pass

def f_max(l):
    n = len(l)
    max_v = l[0]
    min_v = l[0]
    sum_v = l[0]
    for i in range(1, n):
        if l[i] > max_v:
            max_v = l[i]
        if l[i] < min_v:
            min_v = l[i]
        sum_v += l[i]

    print("최소값 :" + str(min_v) + ";" + " 최대값 :" + str(max_v)+ ";" + " SUM값 :" + str(sum_v))
    #print("최대값 :"+str(max_v))
    #print("SUM값 :" + str(sum_v))
    #print(max_v)

    return max_v

def f_min(l):
    n = len(l)
    min_v = l[0]
    for i in range(1, n):
        if l[i] < min_v:
            min_v = l[i]
    print("최소값 :"+str(min_v))
    #print(min_v)

    return min_v

def f_sum(l):
    n = len(l)
    sum_v = l[0]
    for i in range(1, n):
            sum_v += l[i]
    print("SUM값 :"+str(sum_v))
    #print(sum_v)

    return sum_v

l = [12345, 12, 4938338, 1, 3033213, 17]
f_max(l)
#f_min(l)
#f_sum(l)