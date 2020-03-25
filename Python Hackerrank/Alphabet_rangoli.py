def print_rangoli(size):
    # your code goes here
    n = int(size)
    k = 4*n-3
    s = '-'+chr(n+96)+'-'
    for i in range(0,n-1):
        tmp1 = '-'+chr(n+96-i)+'-'
        s = s[:2*i]+tmp1+s[2*i-1:]
        print(s.center(k,'-'))
    a = (s[1:(k//2+1)]+'a'+s[(k//2-2):k-3])
    print(a)
    for j in reversed(range(1,n)):
        tmp2 = '-'+chr(n+96-j)+'-'
        print(s.center(k,'-'))
        s = s[:2*j-3]+s[2*j+1:]
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
