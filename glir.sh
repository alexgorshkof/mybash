#!/usr/bin/env bash
GLOBIGNORE="*"
IFS=$'\n'

function milis() {
#    echo "$1 $(($(date +%s%N)/1000000 % 10000))"
    return 0
}

function glir() {
    milis start
    git fetch

    if [ -z "$1" ]
    then
        local_branches=( $( git branch ) )
        remote_branches=( $(git branch -a))
    else
        local_branches=( $( git branch | grep $1 ) )
        remote_branches=( $(git branch -r | grep $1))
    fi
    milis fetched
    branches=( "${local_branches[@]}" )
    echo "$local_branches"
    echo "---"
    echo "$remote_branches"
    echo "===="

    for remote_branch in "${remote_branches[@]}"
    do :
        add=true
        for local_branch in "${local_branches[@]}"
        do :
            if [[ "$remote_branch"  =~ "$(echo ${local_branch/\*/} | xargs)" ]]; then
                add=false
            fi
        done
        if ${add}; then
            branches+=("$remote_branch")
        fi
    done
    milis looped
    printf '%s\n' "${branches[@]}"

    arr_size=( ${#branches[@]} )
    echo $arr_size

    if (( arr_size > 9 ))
    then
        echo 'too much strings match your query:'
        printf '%s\n' "${branches[@]:0:9}"
        echo "and $(($arr_size-9)) more"
        return 0
    elif (( arr_size == 0 ))
    then
        echo 'no branch matches your query'
        return 0
    elif (( arr_size > 1 ))
    then
        echo "choose one of branches from 0 to $(($arr_size-1))"
        for ((a=0; a < $arr_size; a++))
        do
            echo "$(($a)) : ${branches[$a]}"
        done
        read num
        branch=${branches[$num]}
    else
        echo "one branch match"
        branch=${branches[0]}
    fi

    branch=$(echo ${branch/\*/} | xargs)
    echo "branch '$branch'"
    branch=${branch/remote\//}
    branch=${branch/origin\//}
    echo "branch '$branch'"
    milis end
    git checkout ${branch}

}
#glir master
#glir '102[59]\|10221'