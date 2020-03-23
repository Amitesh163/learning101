if __name__ == '__main__':
    n=int(input())
    marksheet = [[input(),float(input())] for _ in range(n)]
    m = 1000000
    for i in range(n):
        if(marksheet[i][1]*10000<m):
            m=marksheet[i][1]*10000
    for i in range(n):
        if(marksheet[i][1]*10000==m):
            marksheet[i][1]=1000000
    m = 1000000
    s = list()
    c=0
    for i in range(n):
        if(marksheet[i][1]*10000<=m):
            m=marksheet[i][1]*10000
    for i in range(n):
        if(marksheet[i][1]*10000==m):
            s.append(marksheet[i][0])
            c=c+1
    s.sort()
    for i in range(c):
        print(s[i])
   # print(marksheet[c][0])
            

