import sys

from src.Input import Input
from src.Output import Output


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        input_obj = Input(*f.readline().split(" "))
    # print(input_obj)


    # example of output
    v2r = {1: [0,1]}
    o = Output(v2r)
    print(o)



if __name__ == '__main__':
    main()