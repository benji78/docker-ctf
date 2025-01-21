#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void hidden_shell() {
    char flag_base64[] = "ZmxhZ3tiMGZfc2hlbGxfYWNjZXNzfQ==";
    printf("Congratulations! Here is your encoded flag: %s\n", flag_base64);

    system("/bin/sh");
}

int main() {
    char buffer[64];

    printf("Enter some text: ");
    // Use scanf with "%s" so there is no buffer bound checking
    scanf("%s", buffer);

    printf("You entered: %s\n", buffer);

    return 0;
}
