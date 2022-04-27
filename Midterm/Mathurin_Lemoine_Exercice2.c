#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef enum { Reserved , Available } Availability ;
typedef struct{
    int day, month, year;
} date;

void saisiePhrase(char *chaine[], int tailleMax) {

    char *chaineTmp = NULL;
    char c;
    int n = 0;

    chaineTmp = malloc(tailleMax * sizeof(char));
    if (chaineTmp == NULL) {
        printf("Impossible d'allouer de la mémoire");
        exit(0);
    }

    do {
        scanf("%c", &c);
        if (c != '\n' || n != 0) {
            chaineTmp[n] = c;
            n++;
        }
        else {
            c = 0;
        }
    } while (c != '\n' && n < tailleMax);

    n--;
    chaineTmp[n] = 0;

    *chaine = malloc(n * sizeof(char));
    if (*chaine == NULL) {
        printf("Can't allocate memory");
        exit(0);
    }

    strcpy(*chaine, chaineTmp);
    free(chaineTmp);
}

struct Room
{
    char identifier;
    int floor;
    float surface;
    int single_beds;
    int double_beds;
    char input_balcony;
    bool balcony;
    Availability availability;
    date startRentDate;
    date endRentDate;
};

struct Room addRoom() {
    struct Room Room;

    printf("Enter the room's identifier :\n");
    saisiePhrase(&Room.identifier,255);

    printf("Does the room has a balcony? (true/false)\n");
    saisiePhrase(&Room.input_balcony,255);
    if (Room.input_balcony == 't' || Room.input_balcony == 'T') {
        Room.balcony = true;
    } else if (Room.input_balcony == 'f' || Room.input_balcony == 'F') {
        Room.balcony = false;
    } else {
        printf("The answer must be true(T/t) or false(f/F)\n");
        exit(0);
    }

    printf("Enter the room's floor :\n");
    scanf("%d", &Room.floor);

    printf("Enter the room's surface :\n");
    scanf("%f", &Room.surface);
    if (Room.surface < 0) {
        printf("The room's surface must be positive\n");
        exit(0);
    }

    printf("Enter the number of single beds :\n");
    scanf("%d", &Room.single_beds);
    if (Room.single_beds < 0) {
        printf("The number of single beds must be positive\n");
        exit(0);
    }

    printf("Enter the number of double beds :\n");
    scanf("%d", &Room.double_beds);
    if (Room.double_beds < 0) {
        printf("The number of double beds must be positive\n");
        exit(0);
    }


    printf("Enter the room's availability :\n");
    scanf("%d", &Room.availability);

    if (Room.availability == Reserved) {
        printf("Enter the room's start rent date :\n");
        scanf("%d", &Room.startRentDate.day);
        scanf("%d", &Room.startRentDate.month);
        scanf("%d", &Room.startRentDate.year);

        printf("Enter the room's end rent date :\n");
        scanf("%d", &Room.endRentDate.day);
        scanf("%d", &Room.endRentDate.month);
        scanf("%d", &Room.endRentDate.year);
        if (Room.startRentDate.year <= Room.endRentDate.year) {
            if (Room.startRentDate.month <= Room.endRentDate.month) {
                if (Room.startRentDate.day <= Room.endRentDate.day) {
                    return Room;
                }
                else {
                    printf("The start rent date is after the end rent date\n");
                }
            }
            else {
                printf("The start rent date is after the end rent date\n");
            }
        }
        else {
            printf("The start rent date is after the end rent date\n");
        }
    }
}

void main() {
    struct Room Room;
    Room = addRoom();
    printf("%c %d %f %d %d %d %d %d %d %d\n", Room.identifier, Room.floor, Room.surface, Room.single_beds, Room.double_beds, Room.balcony, Room.availability);
    if (Room.availability == Reserved) {
        printf("%d %d %d\n", Room.endRentDate.day, Room.endRentDate.month, Room.endRentDate.year);
    }


}