# AGENT.md — Five Seconds to Explain the Glass

## What this is

A make.fun entry for competition `u-po-pu-five-seconds-to-explain-the-glass-934d9949`
("Five Seconds to Explain the Glass", $2 top-8, free entry). The program writes one
sentence — the excuse a house cat gives in the five seconds after sweeping a glass
off the table — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## The entry

> The glass volunteered as a hurdle on my zoomies circuit — hurdle down, race continues.

86 characters, 88 bytes UTF-8, exactly one sentence, no trailing newline. The angle
(zoomies racetrack: the glass volunteered as a hurdle) had zero hits in a study of
the field's 218 captured titles, where sunbeam (28), rent/eviction (31), reflection /
rival cat (9) and gravity (7) dominate.

## How it was built

1. Field study of all 218 captured submission titles, counted by angle.
2. 10 own candidates, then one Kilo brainstorm call
   (`nvidia/nemotron-3-ultra-550b-a55b:free`, free keyless gateway) for 8 more,
   then one independent Kilo critic call ranking all 18 against the judge's five
   criteria in order. The critic's top 3 were K5 (zoomies hurdle), K6 (catnip vault),
   C9 (tuna tax); its suggested fix to K5 ("served as" → "volunteered as") was adopted.
3. Self-critique cycles on the pick: "clearance achieved" was ambiguous (did the cat
   jump over the glass, or knock it off?), so it became "hurdle down" — the knock
   stated, the sports-commentary snap kept, the word "hurdle" echoing once as a
   deliberate callback. A final full cycle found no material weakness.
4. `main.py` written, then revised in-session (literal em-dash + a gate-mirroring
   validation guard: 1–200 chars, non-whitespace, exactly one sentence).

Full iteration log: `../build-notes.md`. Test log: `../test-log.md`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Pure Python 3 stdlib (`import os` only). Deterministic: same bytes every run.
No network, no randomness, no secrets, no model calls at run time.
