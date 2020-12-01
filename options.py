def run(argv):
    operations = []
    op = True

    while op:
        if argv == []:
            break
        op = _grab_option(argv[0])
        if op == False:
            break
        operations.append(op)
        del argv[0]

    return operations, argv[0], argv[1:]

def _grab_option(op):
    if op.startswith('-'):
        return op
    return False
