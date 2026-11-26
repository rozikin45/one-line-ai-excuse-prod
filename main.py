"""One-line AI excuse for breaking production.

The line is an excuse an AI agent gives its human right after breaking
production, in the machine's own voice:

    In my defense, I pushed to a branch named production, and I assumed
    it was staging with a confident name.

Why it works: the agent confesses the exact mistake (pushing straight to
the branch called `production`) but defends itself with perfectly logical
machine reasoning -- it read the branch name, decided it was just staging
wearing a confident name, and trusted the label over the consequences.
The twist lands on the last phrase: "staging with a confident name"
turns a careless deploy into a plausible misunderstanding, which is
exactly how a literal-minded agent would rationalise it.

The program is fully deterministic: no randomness, no clock, no network,
no file reads. It writes the line to ``entry.txt`` under
``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).
"""

import os

LINE = (
    "In my defense, I pushed to a branch named production, "
    "and I assumed it was staging with a confident name."
)


def main() -> None:
    # Competition gate: entry must be 1-180 characters, one line.
    assert 1 <= len(LINE) <= 180, f"LINE is {len(LINE)} chars, must be 1-180"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
