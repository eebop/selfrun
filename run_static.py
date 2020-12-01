__import__('<pythonfile>')
import sys
#def EXEC_BASH(string):

def EXEC_PY(string):
    exec(string, sys.modules['<pythonfile>'].__dict__)

EXEC_PY('x = 1')
EXEC_PY('print(x)')
