import sys


def main():
    types = [
        'Binary left operator right',
        'Grouping expression',
        'Literal value',
        'Unary operator right'
    ]

    generateAST(types, sys.argv[1])


def generateAST(types, outputdir='../src'):
    path = outputdir + '/Expr.py'
    outfp = open(path, 'w')

    print('', file=outfp)
    print('class Expr():', file=outfp)
    print('    def __init__(self):', file=outfp)
    print('        pass', file=outfp)
    print('', file=outfp)
    print('', file=outfp)
    

    for t in types:
        t = t.split()
        args = ', '.join(t[1:])
        print('class ' + t[0] + '(Expr):', file=outfp)
        print('    def __init(self, ' + args + '):', file=outfp)

        for tt in t[1:]:
            print('        self.' + tt + ' = ' + tt, file=outfp)
        
        print('', file=outfp)
        print('', file=outfp)
    outfp.close()


if __name__ == '__main__':
    main()


'''
class Expr():
    def __init__(self):
        pass

class Binary(Expr):
    def __init__(self, left, operator, right)
        pass
'''