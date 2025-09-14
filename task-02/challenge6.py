t=int(input())
for i in range(t):
    N=int(input())
    a=list(map(int,input().split()))
    freq={}
    for j in range(N):
        if a[j] in freq:
            freq[a[j]]+=1
        else:
            freq[a[j]]=1
    print(len(a)-max(freq.values()))
        
        