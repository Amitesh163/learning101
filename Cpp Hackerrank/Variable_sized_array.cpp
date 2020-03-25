#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int row_count, query_count;
    int column_count,x;
    vector<int> v[1000000];
    long long unsigned int r,c;
    scanf("%d %d\n",&row_count,&query_count);
    for(int i=0;i<row_count;i++){
        scanf("%d",&column_count);
        for(int j=0;j<column_count;j++){
            scanf("%d",&x);
            v[i].push_back(x);
        }
    }
    for(int k=1;k<=query_count;k++){
        scanf("%d %d ",&r,&c);
        printf("%d\n",v[r].at(c));
    }
    return 0;
}
