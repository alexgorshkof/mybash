#!/usr/local/bin/python3.7
import os
import sys


def main(files):
    myCmd = os.popen('git branch ').read()
    print(myCmd)


if __name__ == '__main__':
    print(sys.argv)
    for index, arg in enumerate(sys.argv):
        print(index, arg)
