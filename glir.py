#!/usr/local/bin/python3.7
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
            all_branches = list(filter(lambda branch: name_part.lower() in branch.lower(), all_branches))
            local_branches = list(filter(lambda branch: name_part.lower() in branch.lower(), local_branches))

    # print(f'branches: {branches}')
    # print(f'local branches: {local_branches}')
    # print(f'all_branches: {all_branches}')

    branches = sorted(set(local_branches + all_branches))

    current_branch = next((branch for branch in branches if '*' in branch), None)
    if current_branch:
        current_branch = current_branch.replace('*', '').strip()
        branches.remove(current_branch)

    branch = select_branch(branches)

    if branch:
        new_branch = branch.replace('remotes/origin/', '')
        print(f'checking out branch {new_branch}')

        os.system(f'git checkout {new_branch}')

    return


if __name__ == '__main__':
    main(sys.argv)
