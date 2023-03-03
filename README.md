# Advent of Code Solutions
Advent of Code solutions in various languages - https://adventofcode.com/

## Get Started

```shell
$ git clone https://github.com/coder-trev/advent-of-code.git
```

### Python

Set environment variable `AOC_SESSION="session=<YOUR SESSION TOKEN>"`. I put mine in my `~/.bashrc` file for persistence. You can pull your session token from the developer tools when you login to the advent of code website.

Run `bin/get-puzzle.sh` to pull resources and create a starter script. Pass in the target year and the day.

```shell
$ cd python
$ bin/get-puzzle.sh 2022 1
$ vim 2022/1/main.py
```

## Roadmap

Features:

* common tool to pull puzzle text and input text. It should also output a starter code file for each target language.
    * add powershell version for windows hackers

Languages:

* python3
* nodejs
* some form of lisp
    * common lisp
    * racket
    * clojure
    * emacs lisp (be easy to visualize)
* rust
