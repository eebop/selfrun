def run(file):
    with open(file, 'r') as f:
        data = f.read()
    return parse(data)

def parse(data):
    data = data.splitlines()
    data = list(map(lambda o: o.split(), data))
    return data
