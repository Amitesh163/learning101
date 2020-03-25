if __name__ == '__main__':
    N = int(input())
l = list()
for _ in range(N):
    co = input().split()
    if(co[0]=="insert"):
        l.insert(int(co[1]),int(co[2]))
    elif(co[0]=="print"):
        print(l)
    elif(co[0]=="remove"):
        l.remove(int(co[1])) 
    elif(co[0]=="append"):
        l.append(int(co[1]))
    elif(co[0]=="sort"):
        l.sort()
    elif(co[0]=="pop"):
        l.pop()
    elif(co[0]=="reverse"):
        l.reverse()
