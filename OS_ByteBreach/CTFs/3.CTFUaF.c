#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// This function prints the "secret" flag:
void printFlag() {
    puts("Congratulations! Here is your flag: flag{use_after_free_exploit}");
}

int main() {
    // Disable stdout buffering so we see prints immediately
    setbuf(stdout, NULL);

    printf("Welcome to the Use-After-Free Challenge!\n");

    /*
     * 1) Allocate a chunk big enough to hold a function pointer + some data.
     *    We store the pointer at the start. We'll call this pointer array 'fp'.
     */
    typedef void (*func_ptr)();
    func_ptr *fp = malloc(sizeof(func_ptr) + 64);
    if (!fp) {
        perror("malloc");
        return 1;
    }

    // 2) Initialize the function pointer to NULL (or any dummy value).
    *fp = NULL;

    // 3) Free the chunk, but keep 'fp' around => use-after-free vulnerability!
    free(fp);

    // 4) Allocate a new chunk of the **same size**, likely reusing the freed chunk.
    char *buf = malloc(sizeof(func_ptr) + 64);
    if (!buf) {
        perror("malloc");
        return 1;
    }

    printf("Allocated a new buffer at %p\n", (void *)buf);
    printf("Enter up to 72 bytes (including newline):\n");
    /*
     * By entering data carefully, you can overwrite the old memory region,
     * which still corresponds to 'fp' (the function pointer).
     */
    fgets(buf, sizeof(func_ptr) + 64, stdin);

    // 5) Now we "accidentally" call the original function pointer:
    printf("\nCalling the original function pointer...\n");
    (*fp)();  // If user overwrote *fp with &printFlag, it calls printFlag()!

    printf("Done.\n");
    return 0;
}
        
