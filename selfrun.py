#!/usr/bin/env python
import run_static
import tokenize
import options
import sys
__import__('<pythonfile>')

called_with = options.run(sys.argv[1:])
if called_with == ([], '', []):
    raise Exception('Cannot launch file "". NOTE: This will be considered STDIN in a later update')
print(tokenize.run(called_with[1]))

vars = []

exe_always = []
