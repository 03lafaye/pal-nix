# .bashrc
#
# $Author$
# $Date$
# $Revision$
# vi:set fdm=marker sw=4 ts=4:

#-------- Find config path --------# {{{1

PALNIX="$HOME/pal-nix"
PALNIX_RO="$HOME/pal-nix-read-only"

SCRIPT_DIR=$(
if [ -d "$PALNIX" ]; then
    echo "$PALNIX"
elif [ -d "$PALNIX_RO" ]; then
    echo "$PALNIX_RO"
else
    echo '.'
fi
)

#-------- Source global definitions --------# {{{1
if [ -f $SCRIPT_DIR/.git-completion.bash ]; then
    . $SCRIPT_DIR/.git-completion.bash
fi

export PATH=".:/usr/sbin:~/share/bin:$PATH:$SCRIPT_DIR/scripts"
export PATH=`path.sh`
export EDITOR="vim"
export GREP_OPTIONS="--color --exclude-dir=\.svn"

# Make sure sudo uses the same path
alias sudo='sudo env PATH=$PATH'

set -o notify
set -o noclobber
set -o ignoreeof
set -o vi # set vi commandline mode

bind 'set bell-style none' # turns off annoying command line bell

if [ ! -n "${TERM}" ]; then
    TERM=cygwin
fi

#-------- Source user definitions --------# {{{1

if [ "$COMPUTERNAME" = 'VEGETO' -o "$COMPUTERNAME" = 'SHENRON' ]; then
    source $SCRIPT_DIR/shenron.bashrc
fi

if [ "$COMPUTERNAME" = 'SANGOHAN' ]; then
    source $SCRIPT_DIR/sangohan.bashrc
fi

if [ "$COMPUTERNAME" = 'SANGOTEN' ]; then
    source $SCRIPT_DIR/sangoten.bashrc
fi

#-------- Aliases and Functions --------#  {{{1

alias h="pd ~"  # go home
alias c="clear" # clean up
function pd() { pushd "$1" 1> /dev/null; } # push directory on to stack
alias bk="popd 1> /dev/null" # pop directory from stack
# The 'ls' family
alias ls="ls -F -G"
alias la="ls -aF"
alias ll="ls -lh"
alias lx="ls -lXB" # sort by extension
alias lc="ls -lcr" # sort by change time
alias lr="ls -lR"  # recursive ls
alias lt="ls -ltr" # sort by date
function lm() { ll "$*" | awk '{print $6, $7, $8}'; } # last modification date for a file
alias background="xv -root -quit -max -rmode 5"
alias brc="vim '$SCRIPT_DIR/.bashrc'"
alias sbrc=". '$SCRIPT_DIR/.bashrc'"
alias chmodd="find . -type d -print | xargs chmod 775"
alias chmodf="find . -type f -print | xargs chmod 664"
alias rmsvn="find . -name .svn -exec rm -rf {} \;"
alias hgrep="history | grep "
alias df="df -Th"
alias du="du -h"
alias mkdir="mkdir -p" # prevents accidental clobbers
alias path="echo -e ${PBH//:/\\n}"
alias trix="vim '$SCRIPT_DIR/unixtricks'"
alias vrc="vim '$SCRIPT_DIR/.vimrc'"
# Vim aliases
alias v="vim"
alias vi='vim'
# Start Vim with cscope commands
function vf() { vim -c "cs find f ""$1"; }
function vs() { vim -c "cs find s ""$1"; }
function vg() { vim -c "cs find g ""$1"; }
function vd() { vim -c "cs find d ""$1"; }
function ve() { vim -c "cs find e ""$1"; }
alias gits='git svn'
function gmysql() { /usr/bin/mysql -b -D "$1" -u "$2" -p; }
alias wgetsite="wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --no-parent"
alias g++d="g++ -g -O0 -fno-inline"
alias gccd="gcc -g -O0 -fno-inline"
alias gitbr='for k in `git branch | perl -pe s/^..//`; do echo -e `git show --pretty=format:"%Cgreen%ci %Cblue%cr%Creset" $k -- | head -n 1`\\t$k; done | sort -r'
alias cpl="find . -name '*.mp3' -execdir bash -c 'file=\"{}\"; printf \"%s\n\" \"${file##*/}\" >> \"${PWD##*/}.m3u\"' \;"

#-------- Colors  --------# {{{1

red="\[$(tput setaf 1)\]"
blue="\[$(tput setaf 4)\]"
cyan="\[$(tput setaf 6)\]"
purple="\[$(tput setaf 5)\]"
green="\[$(tput setaf 2)\]"
white="\[$(tput setaf 7)\]" # white

#-------- Shell Prompt --------# {{{1

A=${cyan}
B=${purple}
C=${green}
NC='\e[0m' # no color

# Add git branch to command prompt

function parse_git_branch
{
  ref=$(git symbolic-ref HEAD 2> /dev/null)

  # Check if mercurial repo
  if [ ! -z "${ref}" ]; then
    ref=$(_dotfiles_scm_info 2> /dev/null)
    ref=${ref//\(}
    ref=${ref//\)}
    ref=${ref// }
  fi

  if [ -z "${ref}" ]; then
    echo $ref
    return
  fi

  echo " ("${ref#refs/heads/}")"
}

function fastprompt()
{
    unset PROMPT_COMMAND
    case $TERM in
        *term | rxvt )
            PS1="\[${A}\][$HOSTNAME]\[${NC}\] \W\$(parse_git_branch) > " ;;
        linux )
            PS1="\[${A}\][$HOSTNAME]\[${NC}\] \W\$(parse_git_branch) > " ;;
        * )
            PS1="\[${C}\][$HOSTNAME]\[${NC}\] \W\$(parse_git_branch) > " ;;
    esac
}

function nocolorprompt()
{
    unset PROMPT_COMMAND
    PS1="[$HOSTNAME] \W\$(parse_git_branch) > "
}

nocolorprompt
# fastprompt
