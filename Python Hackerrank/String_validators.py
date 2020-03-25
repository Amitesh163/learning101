if __name__ == '__main__':
    s = input()
    f=0
    g=0
    h=0
    x=0
    j=0
    for i in range(0,len(s)):
        if('a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<=s[i]<='9'):
            f=f+1
        if('a'<=s[i]<='z' or 'A'<=s[i]<='Z'):
            g=g+1
        if('0'<=s[i]<='9'):
            h=h+1
        if('a'<=s[i]<='z'):
            x=x+1
        if('A'<=s[i]<='Z'):
            j=j+1
    if(f>0):
        print("True")
    else:
        print("False")
    if(g>0):
        print("True")
    else:
        print("False")
    if(h>0):
        print("True")
    else:
        print("False")
    if(x>0):
        print("True")
    else:
        print("False")
    if(j>0):
        print("True")
    else:
        print("False")

