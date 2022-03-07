#include <stdio.h>

int prime (int n) {
    if(n ==2) return 1;
    else {
        int k =2; int z =1;
        while (k <n) {
            while (( prime (k) ==0) &&( k <n -1) ) {k ++;};
            if (n %k ==0) { z =0; k ++;} else k ++;
        };
        return z;
    };
}
void main () {
    int i;
    for (i =2; i <30; i++)
    if (prime(i) == 1)
        printf("%d\n",i);
    else
    continue;
}