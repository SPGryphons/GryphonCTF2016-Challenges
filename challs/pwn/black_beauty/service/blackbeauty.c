#include <stdio.h>
#include <stdlib.h>

struct ticker_tape {
    unsigned int length;
    char symbol[8];
    char tape[128];
};

void tape_machine(int user_length) {
    struct ticker_tape user_tape;
    user_tape.length = user_length;
    strcpy(user_tape.symbol, "NOOB");
    int position = 0;
    int running = 1;
    int choice = 0;
    int i = 0;
    while (running) {
        puts("Ticker Tape Menu:");
        puts("1) Print stock values");
        puts("2) Write value");
        puts("3) Seek to position");
        puts("\n0) Exit");
        scanf("%d", &choice);
        if (choice == 0) {
            running = 0;
        }
        else if (choice == 1) {
            puts(user_tape.symbol);
            for (i = 0; i < user_tape.length; i++) {
                printf("#%d\n", user_tape.tape[i]);
            }
        }
        else if (choice == 2) {
        }
        else if (choice == 3) {
        }
    }
}

int main() {
    puts("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");
    puts("% Nothing my sparrow, blue.  %");
    puts("%     Oh what can I do?      %");
    puts("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");
    puts("% Stock Ticker Tape Program  %");
    puts("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");

    int user_length = 0;
    printf("Please enter your ticker tape length: ");
    scanf("%d", &user_length);
    if (user_length > 128 || user_length < 0) {
        puts("We don't have enough space to store your ticker tape.");
    }
    else {
        tape_machine(user_length);
    }
}
