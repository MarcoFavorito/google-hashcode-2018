import sys

from src.Input import Input


def main():
    filename = sys.argv[0]
    with open(filename) as f:
        input_obj = Input(*f.readline().split())




if __name__ == '__main__':
    main()