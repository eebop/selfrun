import os
if os.path.exists('hasran'):
    HASRAN = True
else:
    HASRAN = False
    os.system('chmod +x run_once.sh')
    os.system('./run_once.sh')
