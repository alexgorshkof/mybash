#!/usr/local/bin/python3.7
import os
import sys
from gli import *


def main(params):
    print("fetching remote branches:")
    os.system('git fetch')
    print("done")

    all_branches = format_branches(os.popen('git branch -a').read().split("\n"))

    local_branches = format_branches(os.popen('git branch').read().split("\n"))

    if len(params) > 1:
        name_part = params[1]
        if name_part:
            all_branches = list(filter(lambda x: name_part in x, all_branches))
            local_branches = list(filter(lambda x: name_part in x, local_branches))

    branches = local_branches.copy()
    for branch in all_branches:
        add = True
        for local_branch in local_branches:
            if '*' in local_branch:
                local_branch = local_branch.replace('*', '').strip()
            if local_branch in branch:
                add = False
                break
        if add:
            branches.append(branch)

    branch = select_branch(branches)

    new_branch = branch.replace('remotes/origin/', '')
    print(f'checking out branch {new_branch}')

    os.system(f'git checkout {new_branch}')
    return


if __name__ == '__main__':
    main(sys.argv)
