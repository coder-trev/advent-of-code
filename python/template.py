#!/usr/bin/env python3

import os, sys, re
#from collections import 
from pprint import pprint as pp

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'input.py')) as f:
    lines = f.readlines()
    pp.print(lines)
