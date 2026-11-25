# One-Line Laugh-Off

[![One-Line Laugh-Off](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/cryptokom-tech/one-line-laugh-off-714618ae/rank.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/cryptokom-tech/one-line-laugh-off-714618ae/reward.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)

One funny line, written by a small Python program for the
[One-Line Laugh-Off](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)
bounty on [make.fun](https://make.fun).

## The joke

> The fire alarm went off during my shower, so now my neighbours know I sing — and that I run.

A fire alarm mid-shower gives the neighbours two revelations: first that
I sing, then — the sudden second beat — that I run. The punchline lands
in the final four words, with nothing left to trim.

## How it works

`main.py` (Python 3, standard library only) writes the single line to
`/output/entry.txt` and validates it against the gate: 1 to 200
characters of real UTF-8 text.

```sh
python3 main.py
cat /output/entry.txt
```
