def merge_the_tools(string, k):
    # your code goes here
    c = 0
    n = len(string)
    temp = list()
    for i in range(n//k):
        temp.clear()
        for j in string[c:c+k]:
            temp.append(j)
        s = ''
        for x in temp:
            if x not in s:
                s = s + x
        print(s)
        c=c+k 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
