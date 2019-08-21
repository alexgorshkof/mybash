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

    current_branch = next(x for x in local_branches if '*' in x)

    branches = sorted(set(local_branches + all_branches))
    branches.remove(current_branch.replace('*', '').strip())

    # print(f'branches: {branches}')
    # print(f'local branches: {local_branches}')
    # print(f'all_branches: {all_branches}')

    branch = select_branch(branches)

    new_branch = branch.replace('remotes/origin/', '')
    print(f'checking out branch {new_branch}')

    os.system(f'git checkout {new_branch}')
    return


if __name__ == '__main__':
    main(sys.argv)
