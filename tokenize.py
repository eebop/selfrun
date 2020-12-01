def run(file):
    with open(file, 'r') as f:
        data = f.read()
    return parse(data)

def parse(data):
    return data.splitlines()
