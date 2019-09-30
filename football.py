# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[0,0]
    for i in range(n):
        a,b,c=map(int,input().split())
        if a==1:
            print("YES")
            l[0]=b
            l[1]=c
        else:
            if(b==c):
                print("YES")
                l[0]=b
                l[1]=c
            else:
                if (b>=l[0] and c>=l[0]) and (b>=l[1] and c>=l[1]):
                    print("NO")
                else:
                    print("YES")
                    if b>l[0] and c>l[1]:
                        l[0]=b
                        l[1]=c
                    else:
                        l[0]=c
                        l[1]=b