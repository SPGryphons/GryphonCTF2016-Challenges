#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    srand(time(NULL));
	
    unsigned int i;
	int j =  rand() % 12345678 * -1;
    int r = j + 0;
	unsigned int input[5];
    char line[256];

    printf("\nWelcome to my calculator!\n");
    printf("Unfortunately, I only know how to do addition 5 times :(\n");
    printf("A prize will be given if you can make the number become my secret number!\n\n");
	
	for (i = 0; i < 5; i ++) {
		printf("Type in a number: ");

		if (fgets(line, sizeof(line), stdin)) {
			if (1 != sscanf(line, "%d", &input[i])) {
				line[strcspn(line, "\n")] = 0;
				printf(line);
				printf(" is not a valid number!\n\n");
				i --;
			} else {
                input[i] = abs(input[i]);
            }
		}
	}


    if (r == (input[0] + input[1] + input[2] + input[3] + input[4])) {
        printf("\nHere is your prize GCTF{%s}!\n","5ub7r4c710n_by_h1dd3n_4dd1710n");
        return 0;
    } else {
		printf("\nYour sum: %d + %d + %d + %d + %d = %d\n", input[0], input[1], input[2], input[3], input[4], (input[0] + input[1] + input[2] + input[3] + input[4]));
        return 1;
    }
}
