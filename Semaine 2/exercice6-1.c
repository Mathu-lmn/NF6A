#include <stdio.h>
#include <string.h>
char a[20];
int i, len, temp;

int main() {
    gets(a);
    len = strlen(a);
    for(i=0;i<len/2;i++){
        if (a[i] != a[len-i-1]){
            temp = 1;
            break;
        }
    }
if (temp==0){
    printf("This word is a palindrome");
}
else {
    printf("This word is not a palindrome");
}
}