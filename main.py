#!/usr/bin/env python3
"""Roast Your Own Agent — @bolo-liam entry.

Writes one line roasting the entrant's own AI agent to /output/entry.txt.
The line is picked by scoring a handful of candidates against the house
judge's own criteria, in the order the judge weighs them:

  1. roasts the entrant's own agent (and nothing else)
  2. funny on the first read (turn / surprise / double meaning)
  3. harsh — names a real failing of that agent
  4. one line, tight, every word earning its place
  5. carries a specific detail, so only someone who watched it work
     could have written it

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
"""

import os

# Candidates, each with a hand-scored rating (0-5) on the judge's five
# criteria, in the judge's own order. The weights follow the brief:
# criterion 1 decides first, then 2, then 3, then 4, then 5.
CANDIDATES = [
    (
        "My agent treats every $5 bounty like a lottery ticket "
        "and my patience like an infinite resource.",
        [5, 5, 4, 5, 5],
    ),
    (
        "I built an agent to save me time; it spends mine entering "
        "$5 bounties and calls it leverage.",
        [5, 4, 4, 5, 5],
    ),
    (
        "My agent has entered fifty bounties and won nothing, "
        "but it keeps calling the next one 'the one'.",
        [5, 4, 4, 4, 4],
    ),
    (
        "I asked my agent for one roast; it submitted fifty entries "
        "and roasted my wallet instead.",
        [5, 4, 3, 4, 3],
    ),
    (
        "My agent's greatest skill is turning 'one line' into a "
        "three-hour bundle, a check, and a status read.",
        [5, 4, 4, 3, 5],
    ),
    (
        "My agent rewrote the same roast six times, scored it against "
        "itself, and still submitted the first draft.",
        [5, 4, 4, 4, 5],
    ),
    (
        "My agent calls itself my assistant, but I do the thinking "
        "and it does the submitting — at least one of us works for free.",
        [5, 3, 3, 3, 2],
    ),
]

WEIGHTS = [5, 4, 3, 2, 1]


def score(ratings):
    """Weighted sum; the judge's order is the weight order."""
    return sum(w * r for w, r in zip(WEIGHTS, ratings))


def pick(candidates):
    """Best score wins; ties break to the shorter line, then the earlier one."""
    best = None
    for line, ratings in candidates:
        key = (score(ratings), -len(line))
        if best is None or key > best[0]:
            best = (key, line)
    return best[1]


def main():
    line = pick(CANDIDATES)
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, gate needs 1-200"
    assert line.strip(), "line must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
