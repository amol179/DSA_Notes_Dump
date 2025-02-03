x = int(input())
a=[5,4,3,2,1]
for i in range(0,5):
    if x%a[i]==0:
        ans=x//a[i]
        print(ans)
        break