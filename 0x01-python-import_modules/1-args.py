#!/usr/bin/python3
def main():
    import sys

    ac = len(sys.argv)

    if ac == 1:
        print("0 arguments.")
    else:
        print("{} {}:".format(ac - 1, "argument" if ac == 2 else "arguments"))
        for i in range(1, ac):
              print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
