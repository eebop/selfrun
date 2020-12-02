def run(file):
    with open(file, 'r') as f:
        data = f.read()
    return parse(data)

def parse(data):
    data = data.splitlines()
    data = [x for x in data if x != '']
    data = list(map(lambda o: o.split(), data))
    return data
