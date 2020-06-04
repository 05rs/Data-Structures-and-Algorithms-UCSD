# Uses python3


def get_optimal_value(capacity, data):
    value=0
    weight=0
    lis=sorted(data,reverse=True)
    for li in lis:
        if(weight<=capacity):
            v,w=data[li]
            if weight+ w<=capacity:
                weight=weight+ w
                value=value+v
            else:
                x=capacity-weight
                frac=x/w
                weight=weight + frac*w
                value=value+ frac*v
        else:
            break


    return value


n, capacity = (map(int, input().split()))
data={}
for id in range(n):
    value , weight = (map(int, input().split()))
    data[value/weight]=[value,weight]
opt_value = get_optimal_value(capacity, data)
print(opt_value)



# opt_value = get_optimal_value(capacity, weights, values)
# print("{:.10f}".format(opt_value))

