#include <stdio.h>    
     
int main()    
{    
    int arr[] = {45, 5, -5, 8,66};      
        
    int length = sizeof(arr)/sizeof(arr[0]);    
        
    int max = arr[0];    
        
    for (int i = 0; i < length; i++) {     
       if(arr[i] > max)    
           max = arr[i];    
    }      
    printf("Largest element in the array: %d\n", max);    
    return 0;    
}    