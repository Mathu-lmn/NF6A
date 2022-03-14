#include <stdio.h>

void main() {

    int arr[10] = {'2', '1', '6', '5', '6', '1'};

    int i, j, a, n = 6;

    for (i = 0; i < n; ++i) {
        for (j = i + 1; j < n; ++j) {
            if (arr[i] < arr[j]) {

                a = arr[i];
                arr[i] = arr[j];
                arr[j] = a;
            }
        }
    }

    printf("The numbers in descending order are given below\n");

    for (i = 0; i < n; ++i) {
        printf("%c\n", arr[i]);
    }
}