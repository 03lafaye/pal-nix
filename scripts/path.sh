#!/bin/sh

#   "@(#)$Id: clnpath.sh,v 1.6 1999/06/08 23:34:07 jleffler Exp $"
#
#   Print minimal version of $PATH, possibly removing some items

case $# in
0)  chop=""; path=${PATH:?};;
1)  chop=""; path=$1;;
2)  chop=$2; path=$1;;
*)  echo "Usage: `basename $0 .sh` [$PATH [remove:list]]" >&2
    exit 1;;
esac

# Beware of the quotes in the assignment to chop!
echo "$path" |
${AWK:-awk} -F: '#
BEGIN   {   # Sort out which path components to omit
            chop="'"$chop"'";
            if (chop != "") nr = split(chop, remove); else nr = 0;
            for (i = 1; i <= nr; i++)
                omit[remove[i]] = 1;
        }
{
    for (i = 1; i <= NF; i++)
    {
        x=$i;
        if (x == "") x = ".";
        if (omit[x] == 0 && path[x]++ == 0)
        {
            output = output pad x;
            pad = ":";
        }
    }
    print output;
}'
