#!/usr/bin/env bash

YEAR=$1
DAY=$2

API=https://adventofcode.com/$YEAR/day/$DAY
DEST=$PWD/$YEAR/$DAY
PUZZLE=$DEST/puzzle.md
MAIN=$DEST/main.py
INPUT=$DEST/input.py

mkdir -p $DEST

#pull puzzle text
if [[ ! -f $PUZZLE ]]; then
    #TODO: crawl the page and turn the puzzle text into markdown
    #curl $API > $PUZZLE 2> /dev/null
    echo "NOT IMPLEMENTED" > $PUZZLE
fi

# create main file
if [[ -f $MAIN ]]; then
    echo "Oops. Looks like there's already code for 12/$DAY/$YEAR. You'll need to delete $MAIN to start from scratch."
else
    cp template.py $MAIN
fi

#get input
if [[ ! -f $INPUT ]]; then
    curl --cookie "$AOC_SESSION" $API/input > $INPUT 2> /dev/null
fi
