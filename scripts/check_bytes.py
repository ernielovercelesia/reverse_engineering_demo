# check offset 0xA94 content
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "binary" / "custom_elf_fixed.exe"
off = 0xA94  # the same as patch_offset

with open(p, "rb") as f:
    f.seek(off)
    print("Bytes at offset 0xA94:", f.read(8).hex())
