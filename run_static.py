__import__('<pythonfile>')
import tokenize
import sys
import os
import re


REPLACE_FOR_FUNC = {
'#': 'HASH'
}

def HASH(string):
    pass

def EXEC_RUN(string):
    exec(string, sys.modules[__name__].__dict__)

def EXEC_BASH(string):
    os.system(string)

def EXEC_PY(string):
    exec(string, sys.modules['<pythonfile>'].__dict__)

def EXEC_ONCE(string):
    exec(string, sys.modules['__main__'].__dict__)

def EXEC_ALWAYS(string):
    sys.modules['__main__'].exe_always.append(string)


exceptable = ['EXEC_BASH', 'EXEC_PY', 'EXEC_ONCE', 'EXEC_ALWAYS', 'EXEC_RUN', '#'] # ADD NEW ONES AT THE END, NOT THE FRONT
def run(line):
    if line and line[0] and line[0][0] == '\n':
        line[0] = line[0][1:]
    print(line)
    global name
    name = line[0]
    matched = match_all(line[0])
    if not matched:
        raise Exception(f'unknown instruction::"{line[0]}"')
    getattr(sys.modules[__name__], replace_all(matched))(' '.join(line[1:]))

def match_all(string):
    for test in exceptable:
        if re.match(test, string):
            return test
    return False

def replace_all(string):
    for key, value in REPLACE_FOR_FUNC.items():
        string = string.replace(key, value)

    return string
