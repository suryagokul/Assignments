def fun(elements, N, K):
    Moving_ave = []
    for i in range(N-K+1):
        Moving_ave.append(sum(elements[i:i+4])/4)

    print("MOVING AVERAGE VALUES", Moving_ave)
    print("LENGTH OF MOVING AVERAGE SEQUENCE", len(Moving_ave))


elements = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

N, K = len(elements), 4

fun(elements, N, K)

