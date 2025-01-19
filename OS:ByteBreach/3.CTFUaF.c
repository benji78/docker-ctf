#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    
    char *data = malloc(32);

    
    strcpy(data, "ZmxhZ3toYXJkX3VhZn0=");

    
    free(data);
    printf("Memory Freed...\n");

    char *another = malloc(32);
    strcpy(another, "Some new data...");


    printf("Data pointer (stale): %s\n", data);

    return 0;
}
