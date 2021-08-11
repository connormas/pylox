import sys

import scanner as sc

def main():
    if len(sys.argv) > 2:
        print('Error: Too many source files provided.', file=sys.stderr)
        print('Usage: python3 pylox.py [source]', file=sys.stderr)
        sys.exit()
    elif len(sys.argv) == 2:
        runFile(sys.argv[1])
    else:
        repl()


def run(source):
    print('SOURCE: ' + source)
    scannner = sc.Scanner(source)
    tokens = scannner.scanTokens()

    # just for now
    for tok in tokens:
        print(tok.lexeme, tok.toktype)

def runFile(filename):
    with open(filename, 'r') as file:
        data = file.read()
        run(data)

def repl():
    hadError = False
    while True:
        try:
            line = input('> ')
            run(line)
        except EOFError:
            print('')
            hadError = True
            break
    

if __name__ == '__main__':
    main()