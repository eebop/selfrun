#!/usr/bin/env python
import run_static
import tokenize
import options
import sys
import os
__import__('<pythonfile>')
called_with = options.run(sys.argv[1:])
if called_with == ([], '', []):
    raise Exception('Cannot launch file "". NOTE: This will be considered STDIN in a later update')
exe_always = []
def run(file):
    code = tokenize.run(file)
    print(code)

    vars = []

    for line in code:
        run_static.run(line)
        for string in exe_always:
            run_static.EXEC_ONCE(string)
run(__file__[:__file__.rfind('/')] + '/launch.sr')
run(called_with[1])
