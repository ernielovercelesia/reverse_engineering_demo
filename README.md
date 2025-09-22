## Reverse Engineering Demo - Firmware/Binary Analysis by Ian-Rung Huang on Sep 23 2025
This repository contains a small reverse engineering demo to showcase my RE skills.

## Prerequisites
- Download the installer from msys2 https://www.msys2.org/ for installing mingw-w64 GCC. Then you can compile custom_elf in binary folder.
- Download Java JDK from https://adoptium.net/ for using Ghidra (ghidraRun.bat).

## Target Binary
- A small ARM ELF binary compiled from C (hello + license check function).
- Purpose: Demonstrate static and dynamic analysis.

## Tools Used
- Ghidra (static analysis)
- Python (patching / automation)

## Analysis Summary
- The binary contains a simple license verification function.
- By analyzing the assembly in Ghidra, I identified the comparison logic.
- I wrote a Python script to patch the binary, bypassing the check.

## Repo Structure
- `/binary` → Original ELF file and the fixed ELF file
- `/analysis` → Ghidra screenshot
- `/scripts` → Python script for patching
- `report.md` → Detailed notes
- `src` → Generate custom_elf.exe

## Disclaimer
This demo binary is self-compiled for learning purposes.  
No proprietary or illegal firmware is used.

## [IMPORTANT]How to demo
- Click custom_elf.exe and enter "license12345" to get Access Granted. Any other input will result in Access Denied.
- Execute /scripts/fix_patch.py; custom_elf_fixed.exe will be generated and replace the original file.
- Click custom_elf_fixed.exe and enter any input—you will always get Access Granted.
- /scripts/check_bytes.py can be used to verify the bytes; running this script is optional.
- A screenshot is provided to illustrate this.