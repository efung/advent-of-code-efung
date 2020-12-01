# Advent of Code Solutions

These solutions are set up according to the guidelines in https://github.com/wimglenn/advent-of-code-sample
which makes use of the `aoc` runner script.

## Setup
After cloning this repository, install the module:

```bash
$ pip install advent-of-code-efung/
```

## Testing individual day's solution

(Optional) Update the test data in each day's file. Make sure to use strings for output!

```bash
$ export AOC_SESSION=<session cookie from browser session>
$ cd aoc_efung/aoc2020
$ python day1.py
```

## Submitting

```bash
$ export AOC_SESSION=<session cookie from browser session>
$ ipython
```

The `submit` function can infer what day and part to submit, but can also specify explicitly via named params.

```python
from aocd import submit

submit(my_answer, part="a", day=1, year=2020)
```
