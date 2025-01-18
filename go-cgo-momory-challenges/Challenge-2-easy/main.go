package main

import (
	"fmt"
	"os"
	"strconv"
	"unsafe"
)

var sensitiveData = []byte{
	0x42, 0x65, 0x65, 0x70, 0x20, 0x42, 0x6F, 0x6F, // "Beep Boo"
	0x70, 0x21, 0x20, 0x53, 0x65, 0x63, 0x72, 0x65, // "p! Secre"
	0x74, 0x20, 0x64, 0x61, 0x74, 0x61, 0x20, 0x2E, // "t data ."
	0x2E, 0x2E, 0x00, // "...\0"
}
var secret = "FLAG{Bravo_tu_as_lu_le_secret_en_memoire}"

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: ./vuln <offset>")
		os.Exit(1)
	}

	offsetStr := os.Args[1]
	offset, err := strconv.Atoi(offsetStr)
	if err != nil || offset < 0 {
		fmt.Println("Offset invalide")
		os.Exit(1)
	}

	ptr := unsafe.Pointer(&sensitiveData[0])
	vulnPtr := unsafe.Pointer(uintptr(ptr) + uintptr(offset))

	if uintptr(vulnPtr) < uintptr(ptr) || uintptr(vulnPtr) >= uintptr(ptr)+uintptr(len(sensitiveData))+4096 {
		fmt.Printf("Offset hors limites (%d)\n", offset)
		os.Exit(1)
	}

	value := *(*byte)(vulnPtr)
	fmt.Printf("[*] Lecture à l'offset %d : 0x%02X ('%c')\n", offset, value, value)
}
