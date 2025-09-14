t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    i=c=0
    while i<n:
            if a[i]==0:
                i+=1
            elif c==0 and a[i]==1:
                i+=x
                c=1
            elif c==1 and a[i]==1:
                print("NO")
                break
    else:
        print("YES")