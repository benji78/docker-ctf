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
    // Use fgets instead of gets, specifying the buffer size
    if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        // Remove the newline character added by fgets
        buffer[strcspn(buffer, "\n")] = '\0';
    } else {
        printf("Error reading input.\n");
        return 1;
    }

    printf("You entered: %s\n", buffer);
    return 0;
}
