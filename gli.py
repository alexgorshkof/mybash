#!/usr/local/bin/python3.7
import os
import sys


def select_branch(branches):
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

    result_branch = result_branch.replace('*', '').strip()
    print(f"selected branch '{result_branch}'")
    return result_branch


def format_branches(raw_branches):
    branches = map(lambda x: x.strip(), raw_branches)
    branches = filter(lambda x: x, branches)
    branches = map(lambda x: x.replace('remotes/origin/', ''), branches)
    branches = list(branches)
    return branches


def main(params):
    branches = format_branches(os.popen('git branch ').read().split("\n"))

    if len(params) > 1:
        name_part = params[1]
        if name_part:
            branches = list(filter(lambda branch: name_part.lower() in branch.lower(), branches))

    result_branch = select_branch(branches)

    result_branch = select_branch(branches)
    if result_branch:
        os.popen(f"git checkout {result_branch}")


if __name__ == '__main__':
    main(sys.argv)
