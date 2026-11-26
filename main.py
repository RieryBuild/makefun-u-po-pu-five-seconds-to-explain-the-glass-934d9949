import os

ENTRY = "The glass volunteered as a hurdle on my zoomies circuit — hurdle down, race continues."

# Mirror the sealed gate before writing: one sentence, 1-200 chars, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would score 0.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters, got %d" % len(ENTRY)
assert ENTRY.strip(), "entry must not be only whitespace"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be exactly one sentence"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
