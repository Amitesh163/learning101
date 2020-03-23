def count_substring(string, sub_string):
    c=0
    k=0
    for i in range(0,len(string)-len(sub_string)+1):
        if(sub_string[0]==string[i]):
            c=1
            for j in range(1,len(sub_string)):
                if(sub_string[j]==string[i+j]):
                    c=c+1
            if(c==len(sub_string)):
                k=k+1 
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
