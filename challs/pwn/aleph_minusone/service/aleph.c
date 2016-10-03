#include <stdio.h>
#include <stdlib.h>

void give_shell() {
    system("/bin/sh");
}

void vulnerable() {
    char buffer[128];
    register int bp asm ("bp");
    printf("Base Pointer: %p\n", bp);
    printf("Address of Buffer: %p\n", buffer);
    puts("Size of buffer: 128");
    printf("give_shell() function: %p\n", give_shell);
    printf("Your exploit string: ");
    gets(buffer);
    printf("Contents of Buffer: %s\n", buffer);
    printf("Return Address: %p\n", *(int *)(bp+4));
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    vulnerable();
}
