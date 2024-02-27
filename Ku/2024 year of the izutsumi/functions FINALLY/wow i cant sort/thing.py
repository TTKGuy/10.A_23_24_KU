def readfile(name):
    try:
        with open(name, 'r+', encoding='utf8') as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        print(f'file "{name}" not found')

def readlinee(name):
    try:
        with open(name, 'r+', encoding='utf8') as f:
            contents = f.readline()
            return contents
    except FileNotFoundError:
        print(f'file "{name}" not found')


def readlen(name, len):
    try:
        with open(name, 'r+', encoding='utf8') as f:
            contents = f.read(int(len))
            return contents
    except FileNotFoundError:
        print(f'file "{name}" not found')
    except ValueError:
        print('valueerror')




filename = input("input file name")
fcontent = readfile(filename)

if fcontent:
    print(len(fcontent))
    print(fcontent[0],fcontent[-1])
    print(readlen(filename, input("how many digits")))
    print(readlinee(filename))
    