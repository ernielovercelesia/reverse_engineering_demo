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

## Disclaimer
This demo binary is self-compiled for learning purposes.  
No proprietary or illegal firmware is used.

## [IMPORTANT]How to demo
- Click custom_elf.exe and enter "license12345" you will get access granted. But other words entered, you will get access denied.
- Execute `/scripts/fix_patch.py`, custom_elf_fixed.exe will appear and replace the old one.
- Click custom_elf_fixed.exe and enter any word you will all get access granted.
- `/scripts/check_bytes.py` is for checking the bytes, it optional to click this .py file.
- There is a screenshot showing that 