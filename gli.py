#!/usr/local/bin/python3.7
import os
import sys

if __name__ == '__main__':

    branches = list(map(lambda line: line.strip(), os.popen('git branch ').read().split("\n")))

    if len(sys.argv) > 1:
        name_part = sys.argv[1]
        if name_part:
            print(f"name_part: {name_part}")
            branches = list(filter(lambda branch: name_part in branch, branches))

    print(f"branches: {branches}")
