package main

/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct {
    char buffer[16];
    int isAdmin;
} gData;

void insecureCopy(char *input) {
    strcpy(gData.buffer, input);
    printf("buffer = %s\n", gData.buffer);
}

int getIsAdmin() {
    return gData.isAdmin;
}
*/
import "C"
import (
	"fmt"
	"os"
	"unsafe"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Usage: %s <payload>\n", os.Args[0])
		return
	}
	payload := os.Args[1]
	cPayload := C.CString(payload)
	defer C.free(unsafe.Pointer(cPayload))

	C.insecureCopy(cPayload)

	adminValue := int(C.getIsAdmin())
	if adminValue == 1 {
		fmt.Println("Félicitations, vous êtes devenu admin grâce à la corruption mémoire !")
	} else {
		fmt.Printf("isAdmin = %d\n", adminValue)
	}
}
