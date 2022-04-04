#include <stdio.h>

int loan;

typedef enum { Loaned , Available } bookState ;
typedef struct{
    int day, month, year;
} date;
typedef struct {
    char author [20] ;
    char title [100] ;
    char rib [9] ;
    int year ;
    char editor [20] ;
    bookState state ;
    date loanDate ;
} LibBook ;

LibBook BookInput(){
    LibBook Book;
    printf("Book Author :\n");
    scanf("%s",Book.author);
    printf("Book Title :\n");
    scanf("%s",Book.title);
    printf("Book Rib :\n");
    scanf("%s",Book.rib);
    printf("Book Year :\n");
    scanf("%d",&Book.year);
    printf("Book Editor :\n");
    scanf("%s",Book.editor);
    printf("Is loaned ? (1 : Loaned // 2: Available) \n");
    scanf("%d",&loan);
    if (loan == 1){
        Book.state = Loaned;
        printf("Input the Day of return : ");
        scanf("%d",&Book.loanDate.day);
        printf("Input the Month of return : ");
        scanf("%d",&Book.loanDate.month);
        printf("Input the Year of return : ");
        scanf("%d",&Book.loanDate.year);
    }
    else if (loan == 2) {
        Book.state = Available;
    }
    else printf("Incorrect State Entered, please try again");
    
    return Book;
}

int main() {
    int M,i;
    FILE *ptr;
    char name[20];
    printf("Input a file name : ");
    scanf("%s",name);
    printf("Enter the number of books : ");
    scanf("%d",&M);

    ptr = fopen(name,"w+");
    fprintf(ptr, "%s %d\n", "Number of books entered :",M);
    fprintf(ptr, "Book\t Author\t Title\t Rib\t Year\t Editor\t State\n",i);

    for (i=1; i<M+1; i++){
        fprintf(ptr, "Book %d\t",i);
        LibBook Book = BookInput();
        fprintf(ptr, "%s\t",Book.author);
        fprintf(ptr, "%s\t",Book.title);
        fprintf(ptr, "%s\t",Book.rib);
        fprintf(ptr, "%d\t",Book.year);
        fprintf(ptr, "%s\t",Book.editor);
        if (Book.state == 0)
            fprintf(ptr, "Loaned\n");
        else fprintf(ptr,"Available\n");
    }

    //LibBook Book1 = BookInput();
}