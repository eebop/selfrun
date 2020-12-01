#!/usr/bin/env python
import run_static
import tokenize
import options
import sys

called_with = options.run(sys.argv[1:])

print(tokenize.run(called_with[1]))
