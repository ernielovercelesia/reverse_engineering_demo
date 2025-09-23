# Reverse Engineering Report by Ian-Rung Huang on Sep 23 2025

### Target
- Binary: `custom_elf.exe` (compiled with GCC)
- Function of interest: `main` (contains license check)

### Tools
- Ghidra: disassembly and function decompilation
- Python: binary patching and verification
- C: Making the custom_elf.exe

### Findings
- The binary checks if user input matches `"license12345"`.
- Found the string in the `.rdata` section.
- The `main` function reads user input and calls `strcmp` to compare with the correct license.
- The conditional jump (`JNZ`) after `strcmp` decides whether to print "Access granted!" or "Access denied!".

### Exploit / Patch
- Patched the conditional jump at **file offset `0xA94`**.
- Replaced the 2-byte short jump (`JNZ 0x11`) with NOPs (`90 90`) to force the program to always execute the "Access granted!" branch.
- Result: Any input is accepted as a valid license.

### Scripts
- `/scripts/fix_patch.py` – Python script to apply the patch using relative paths.
- `/scripts/check_bytes.py` – Python script to verify the bytes at the patched off.

### Offset 0xA94 Explanation
The offset 0xA94 marks the start of the check_license function. It is calculated by adding the function’s relative virtual address to the base address of the .text section, ensuring accurate location for analysis.
