#include <stdio.h>
#include <stdbool.h>
#include <string.h>

char a[20];
int i, len, temp;

bool isPalindrome(char a[], int i, int len) {
    if (a[i] != a[len-i-1]){
        return false;
    }
    else if (i<(len/2)){
        i++;
        return isPalindrome(a,i,len);
    }
    return true;
}

int main() {
    gets(a);
    len = strlen(a);
    if (isPalindrome(a,i,len)==1){
    printf("This word is a palindrome");
    }
    else {
    printf("This word is not a palindrome");
    }
}