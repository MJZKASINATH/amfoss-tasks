t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    if Y>=X:
        print(X)
    else:
        print(Y)