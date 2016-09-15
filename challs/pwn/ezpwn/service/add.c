#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    srand(time(NULL));
    int r = rand() % 1000 + 1000;
    int i;
    int tries = 2;
    char line[256];
    
    printf("Welcome to my calculator!\n");
    printf("Unfortunately, I only know how to do addition :(\n");
    printf("A prize will be given if you can make the number become 1000 in 1 try!\n");
    printf("Type in a number (Currently: %d): ", r);

    if (fgets(line, sizeof(line), stdin)) {
        if (1 == sscanf(line, "%d", &i)) {
            r += abs(i);
        }
    }

    if (r == 1000) {
        printf("Here is your prize GCTF{%s}!\n","0v3rfl0w_b4ck_70_7h0u54nd");
    } else {
        printf("Sorry, your end value is %d, not 1000. Try again!\n", r);
    }
}
