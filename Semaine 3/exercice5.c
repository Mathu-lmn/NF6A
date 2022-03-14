#include <stdio.h>

void main() {
    int a,i,position = 0, n = 5;
    int arr[100] = {'4', '6', '7', '9'};
    printf("Enter the item you want to insert : ");
    scanf("%c",&a);
    for (i = 0; i < n;i++) {
        if (arr[i]<a)
        position++;
        else
        break;
    }
    for (i = n-1; i >= position; i--) {
        arr[i+1] = arr[i];
    }
    arr[position] = a;

    for (i = 0; i < n; i++){
        printf("%c\t",arr[i]);
    }
}