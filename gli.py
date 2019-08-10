#!/usr/local/bin/python3.7
import os
import sys


def main(params):
    raw_branches = os.popen('git branch ').read().split("\n")
    branches = list(filter(lambda line: line, raw_branches))

    if len(params) > 1:
        name_part = params[1]
        if name_part:
            print(f"name_part: {name_part}")
            branches = list(filter(lambda x: name_part in x, branches))

    print(f"branches: {branches}")

    if len(branches) > 9:
        print("too much branches match your query")
        for branch in branches[:9]:
            print(branch)
        print(f"and {len(branches) - 9} more")
        return
    elif len(branches) is 0:
        print("no branches match your query")
        return

    elif len(branches) is 1:
        print("one branch match")
        result_branch = branches[0]
    else:
        print("select branch: ")
        for index, branch in enumerate(branches):
            print(f"{index}, {branch}")
        read_index = input()
        result_branch = branches[int(read_index)]

    if '*' in result_branch:
        result_branch = result_branch.replace('*', '').strip()

    print(f"checking out branch: {result_branch}")
    os.popen(f"git checkout {result_branch}")


if __name__ == '__main__':
    main(sys.argv)
