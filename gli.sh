#!/usr/bin/env bash
GLOBIGNORE="*"
IFS=$'\n'
function gli() {
#    echo 'changed'
    ~/mybash/gli.py "$@"
#    if [ -z "$1" ]
#    then
#        branches=( $( git branch ) )
#    else
#        branches=( $( git branch | grep $1 ) )
#    fi
#
#    echo $branches
#    arr_size=( ${#branches[@]} )
#
#    echo $arr_size
#
#    if (( arr_size > 9 ))
#    then
#        echo 'too much strings match your query:'
#        printf '%s\n' "${branches[@]:0:9}"
#        echo "and $(($arr_size-9)) more"
#        return 0
#    elif (( arr_size == 0 ))
#    then
#        echo 'no branch matches your query'
#        return 0
#    elif (( arr_size > 1 ))
#    then
#        echo "choose one of branches from 0 to $(($arr_size-1))"
#        for ((a=0; a < $arr_size; a++))
#        do
#            echo "$(($a)) : ${branches[$a]}"
#        done
#        read num
#        branch=${branches[$num]}
#    else
#        echo "one branch match"
#        branch=${branches[0]}
#    fi
#
#    branch=$(echo ${branch/\*/} | xargs)
#    echo "branch '$branch'"
#
#    git checkout ${branch}
}