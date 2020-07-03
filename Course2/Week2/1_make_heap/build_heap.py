# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []

    while True :
        count=0
        for i in range(len(data)-1,-1,-1):

            L= (2*i) +1
            R= (2*i) +2
            # print(data," i ",i,"  Left: ",L," Right: ",R)
            if L < len(data) and R<len(data):
                if data[L]< data[R]:
                    k=L
                else: k=R

                if data[k]<data[i]:
                    data[i],data[k]=data[k],data[i]
                    swaps.append([i,k])
                    count=1
            elif L < len(data):
                if data[L]<data[i]:
                    data[i],data[L]=data[L],data[i]
                    swaps.append([i,L])
                    count=1
            elif R < len(data):
                if data[R]<data[i]:
                    data[i],data[R]=data[R],data[i]
                    swaps.append([i,R])
                    count=1
        if count==0:
            break
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
