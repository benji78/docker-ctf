#include <stdio.h>
#include <string.h>

int main() {
    
    char buffer[64];
    char secret_base64[] = "ZmxhZ3tleGFzeV9mbXR9";

    printf("Enter your name: ");
    fgets(buffer, sizeof(buffer), stdin);

    // Remove trailing newline
    buffer[strcspn(buffer, "\n")] = '\0';

    // Vulnerable: using user input as the format string
    printf(buffer);
    printf("\n");

    return 0;
}
