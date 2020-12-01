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
    if not argv == []:
        return operations, argv[0], argv[1:]
    else:
        return [], '', []

def _grab_option(op):
    if op.startswith('-'):
        return op
    return False
