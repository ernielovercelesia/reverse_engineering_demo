# fix_patch.py - replace the short JNZ (2 bytes) with NOPs (90 90)
from pathlib import Path

binary = Path(__file__).resolve().parent.parent / "binary" / "custom_elf.exe"
if not binary.exists():
    print("Patched file not found at:", binary)
    raise SystemExit(1)

data = bytearray(binary.read_bytes())

off = 0xA94  # Check file offset
print("Before:", data[off:off+4].hex())

# replace the 2-byte short-jump (75 xx) with NOP NOP (90 90)
data[off] = 0x90
data[off+1] = 0x90

# write to a new file so we keep the _patched as original (or overwrite as you like)
out = binary.with_name(binary.stem + "_fixed.exe")
out.write_bytes(data)
print("Wrote fixed file to", out.name)
print("After:", out.read_bytes()[off:off+4].hex())

